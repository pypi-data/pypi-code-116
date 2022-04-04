import os
import re

from urllib.parse import urlparse

from time import time

from dnastack.auth.authorizers import ClientCredentialsAuth
from dnastack.exceptions import DRSDownloadException
from dnastack.helpers.environments import env
from ..exam_helper import initialize_test_endpoint, ReversibleTestCase, ExtendedBaseTestCase
from dnastack.client.collections_client import CollectionServiceClient, Collection
from dnastack.client.dataconnect_client import DataConnectClient
from dnastack.client.files_client import DrsClient, _module_pandas_available


class TestDrsClient(ReversibleTestCase, ExtendedBaseTestCase):
    """ Test a client for DRS service"""

    # Test-specified

    collection_id = env('E2E_COLLECTION_ID_WITH_BLOBS', None)  # TODO Find the default

    # Set up the client for the collection service
    collection_endpoint = initialize_test_endpoint(CollectionServiceClient.get_adapter_type(),
                                                   env('E2E_COLLECTION_SERVICE_URL',
                                                       default='https://collection-service.viral.ai/'))
    collection_client = CollectionServiceClient.make(collection_endpoint)

    # Set up the client for the data repository service
    # NOTE: We use the collection service for this test as the service implements DRS interfaces.
    drs_endpoint = initialize_test_endpoint(DrsClient.get_adapter_type(),
                                            env('E2E_PROTECTED_DRS_URL',
                                                default='https://collection-service.viral.ai/'))
    drs_client = DrsClient.make(drs_endpoint)

    def setUp(self):
        super(TestDrsClient, self).setUp()
        #self.skip_until("2022-03-16")
        self.output_dir = os.path.join(os.path.dirname(__file__), 'tmp')
        os.makedirs(self.output_dir, exist_ok=True)

    def tearDown(self) -> None:
        super(TestDrsClient, self).tearDown()
        for file_name in os.listdir(self.output_dir):
            if file_name[0] == '.':
                continue
            os.unlink(os.path.join(self.output_dir, file_name))

    def test_download_files(self):
        if not _module_pandas_available:
            self.skipTest('The library pandas is not available for this test.')

        re_table_type = re.compile(r"type\s*=\s*'blob'")

        collection_client = CollectionServiceClient.make(self.collection_endpoint)

        collections = collection_client.list_collections()
        self.assert_not_empty(collections)

        target_collection = [c for c in collections if re_table_type.search(c.itemsQuery)][0]

        items = [
            item
            for item in collection_client.get_data_connect_client(target_collection) \
                .query(f'{target_collection.itemsQuery} LIMIT 20')
        ]
        self.assert_not_empty(items)

        # Define the test DRS URL
        drs_net_location = urlparse(self.drs_endpoint.url).netloc
        drs_urls = []
        expected_file_names = set()
        for item in items:
            item_id = item['id']
            expected_file_names.add(os.path.basename(item['name']))
            drs_urls.append(f'drs://{drs_net_location}/{item_id}')

        # Attempt to download the data.
        self.drs_client.download_files(urls=drs_urls, output_dir=self.output_dir)

        existing_file_names = os.listdir(self.output_dir)
        self.assertGreater(len(existing_file_names), 0)

        download_contents = []
        self.drs_client.download_files(urls=drs_urls, out=download_contents)
        self.assertGreaterEqual(len(drs_urls), len(download_contents))
        for download_content in download_contents:
            self.assert_not_empty(download_content)

        print('Done!')

        # New APIs
        # collection_data_connect_client = collection_client.get_data_connect_client(target_collection)
        # tables = collection_data_connect_client.list_tables()
        # self.assert_not_empty(tables)
        # first_table = tables[0]
        # self.assert_not_empty([row for row in collection_data_connect_client.query(f'SELECT * FROM {first_table.name} LIMIT 10')])

        # # Set up a test collection with blobs
        # # language=sql
        # collection_query = f"SELECT * FROM {self.library_table.name} WHERE type='blob' LIMIT 20"
        #
        # items = [i for i in self.data_connect_client.query(collection_query)]
        #
        # if not items:
        #     self.fail('Precondition failed: No blobs available')
        #
        # collection = self.collection_client.create(Collection.make(f'dnastack-e2e-test-{time()}', collection_query))
        # self.after_this_test(self.collection_client.delete, collection)
        #
        # # Define the test DRS URL
        # drs_net_location = urlparse(self.drs_endpoint.url).netloc
        # drs_urls = []
        # expected_file_names = set()
        # for item in items:
        #     item_id = item['id']
        #     expected_file_names.add(os.path.basename(item['name']))
        #     drs_urls.append(f'drs://{drs_net_location}/{item_id}')
        #
        # # Attempt to download the data.
        # self.drs_client.download_files(urls=drs_urls, output_dir=self.output_dir)
        #
        # existing_file_names = os.listdir(self.output_dir)
        # self.assertGreater(len(existing_file_names), 0)
        #
        # download_contents = []
        # self.drs_client.download_files(urls=drs_urls, out=download_contents)
        # self.assertGreater(len(drs_urls), len(download_contents))
        # for download_content in download_contents:
        #     self.assert_not_empty(download_content)

    def test_downloading_files_with_invalid_urls_raises_error(self):
        self.skip_until("2022-04-15")
        drs_net_location = urlparse(self.drs_endpoint.url).netloc
        with self.assertRaises(DRSDownloadException):
            self.drs_client.download_files(urls=[f'drs://{drs_net_location}/foo-bar'])

        with self.assertRaises(DRSDownloadException):
            self.drs_client.download_files(urls=[f'drs://shiroyuki.com/foo-bar'])

        with self.assertRaises(DRSDownloadException):
            self.drs_client.download_files(urls=[f'drs://qwerty.asdf/foo-bar'])
