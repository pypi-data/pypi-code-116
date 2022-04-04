import re
from time import time

import os

from urllib.parse import urlparse

from dnastack import CollectionServiceClient, DataConnectClient
from dnastack.client.collections_client import Collection
from dnastack.helpers.environments import env
from .base import CliTestCase
from ..exam_helper import initialize_test_endpoint, client_id, client_secret, token_endpoint


class TestDrsCommand(CliTestCase):

    # Test-specified

    # Set up the client for the collection service
    collection_endpoint = initialize_test_endpoint(CollectionServiceClient.get_adapter_type(),
                                                   env('E2E_COLLECTION_SERVICE_URL',
                                                       default='https://collection-service.viral.ai/'))

    # # Set up the client for the data connect service
    # data_connect_endpoint = initialize_test_endpoint(DataConnectClient.get_adapter_type(),
    #                                                  env('E2E_PROTECTED_DATA_CONNECT_URL',
    #                                                      default='https://data-connect-trino.viral.ai/'))
    # data_connect_client = DataConnectClient.make(data_connect_endpoint)

    drs_url = env('E2E_PROTECTED_DRS_URL', default='https://collection-service.viral.ai/')

    # # Find the library table.
    # # NOTE: Assume that the table exists.
    # library_table = [t for t in data_connect_client.iterate_tables() if t.name.endswith('.public.library')][0]

    tmp_path = os.path.join(os.getcwd(), 'test-tmp')
    drs_urls = []

    def setUp(self):
        super().setUp()
        self._configure({
            'drs.authentication.oauth2.client_id': client_id,
            'drs.authentication.oauth2.client_secret': client_secret,
            'drs.authentication.oauth2.grant_type': 'client_credentials',
            'drs.authentication.oauth2.resource_url': self.drs_url,
            'drs.authentication.oauth2.token_endpoint': token_endpoint,
            'drs.url': self.drs_url,
        })

        # Set up the temporary directory.
        self.execute(f'mkdir -p {self.tmp_path}')
        self.after_this_test(self._clear_temp_files)

        self.input_file_path = os.path.join(self.tmp_path, 'object_list.txt')

        if not self.drs_urls:
            re_table_type = re.compile(r"type\s*=\s*'blob'")
            collection_client = CollectionServiceClient.make(self.collection_endpoint)
            collections = collection_client.list_collections()
            target_collection = [c for c in collections if re_table_type.search(c.itemsQuery)][0]

            items = [
                item
                for item in collection_client.get_data_connect_client(target_collection) \
                    .query(f'{target_collection.itemsQuery} LIMIT 20')
            ]

            # Define the test DRS URL
            drs_net_location = urlparse(self.drs_url).netloc
            self.drs_urls = []
            expected_file_names = set()
            for item in items:
                item_id = item['id']
                expected_file_names.add(os.path.basename(item['name']))
                self.drs_urls.append(f'drs://{drs_net_location}/{item_id}')

    def test_download_files_with_cli_arguments(self):
        self.retry_if_fail(self._test_download_files_with_cli_arguments,
                           intermediate_cleanup=lambda: self._clear_temp_files())

    def _test_download_files_with_cli_arguments(self):
        result = self.invoke('files', 'download', '-o', self.tmp_path, *self.drs_urls)
        self.assertEqual(0, result.exit_code)

        file_name_list = [f for f in os.listdir(self.tmp_path) if f != os.path.basename(self.input_file_path)]
        self.assertGreaterEqual(len(self.drs_urls), len(file_name_list))

        for file_name in file_name_list:
            file_path = os.path.join(self.tmp_path, file_name)
            self.assertTrue(os.path.getsize(file_path) > 0, f'The downloaded {file_path} must not be empty.')

    def test_download_files_with_input_file(self):
        self.retry_if_fail(self._test_download_files_with_input_file,
                           intermediate_cleanup=lambda: self._clear_temp_files())

    def _test_download_files_with_input_file(self):
        # Prepare the input file.
        with open(self.input_file_path, 'w') as f:
            f.write('\n'.join(self.drs_urls))

        result = self.invoke('files', 'download', '-i', self.input_file_path, '-o', self.tmp_path)
        self.assertEqual(0, result.exit_code)

        file_name_list = [f for f in os.listdir(self.tmp_path) if f != os.path.basename(self.input_file_path)]

        self._logger.debug(f'file_name_list => {file_name_list}')
        self._logger.debug(f'self.drs_urls => {self.drs_urls}')

        self.assertGreaterEqual(len(self.drs_urls), len(file_name_list))

        for file_name in file_name_list:
            file_path = os.path.join(self.tmp_path, file_name)
            self.assertTrue(os.path.getsize(file_path) > 0, f'The downloaded {file_path} must not be empty.')

    def _clear_temp_files(self):
        self.execute(f'rm -rf {self.tmp_path}/*')
