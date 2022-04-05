import requests
import json
import re
from ..utils.parser import Api, better_object, parse_image, get_hostname
from random import shuffle

Booru = Api()


class E926(object):
    """ E926 wrapper

    Methods
    -------
    search : function
        Search and gets images from e926.

    get_image_only : function
        Gets images, meant just image urls from e926.

    """
    @staticmethod
    def append_obj(raw_object: dict):
        """ Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by e926.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            raw_object[i][
                'post_url'] = f"{get_hostname(Booru.e926)}/posts/{raw_object[i]['id']}"

        return raw_object

    def __init__(self, api_key: str = '', user_id: str = ''):
        """ Initializes e926.

        Parameters
        ----------
        api_key : str
            Your API Key which is accessible within your account options page

        user_id : str
            Your user ID, which is accessible on the account options/profile page.
        """

        if api_key and user_id == '':
            self.api_key = None
            self.user_id = None
        else:
            self.api_key = api_key
            self.user_id = user_id

        self.specs = {'api_key': self.api_key, 'user_id': self.user_id}

    async def search(self, query: str,  block: str = '', limit: int = 100, page: int = 1, random: bool = True):

        """ Search and gets images from e926.

        Parameters
        ----------
        query : str
            The query to search for.

        block : str
            The disgusting query you want to block

        limit : int
            The limit of images to return.

        page : int
            The number of desired page

        random : bool
            Shuffle the whole dict, default is True.

        Returns
        -------
        dict
            The json object returned by e926.
        """

        if limit > 100:
            raise ValueError(Booru.error_handling_limit)

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        if block != '':
            self.query = f"{query} -{block}*"

        else:
            self.query = query

        self.specs['tags'] = str(self.query)
        self.specs['limit'] = str(limit)
        self.specs['page'] = str(page)
        

        self.data = requests.get(Booru.e926, params=self.specs, headers=Booru.headers)
        self.final = json.loads(better_object(
            self.data.json()), encoding="utf-8")

        if 'posts' not in self.final:
            raise ValueError(Booru.error_handling_null)

        try:
            if random:
                self.not_random = E926.append_obj(self.final['posts'])
                shuffle(self.not_random)
                return better_object(self.not_random)

            else:
                return better_object(E926.append_obj(self.final['posts']))

        except Exception as e:
            raise ValueError(f'Failed to get data: {e}')

    async def get_image_only(self, query: str,  block: str = '', limit: int = 100, page: int = 1):

        """ Gets images, meant just image urls from e926.

        Parameters
        ----------
        query : str
            The query to search for.

        block : str
            The disgusting query you want to block

        limit : int
            The limit of images to return.

        page : int
            The number of desired page

        Returns
        -------
        list
            The list of image urls.

        """

        if limit > 100:
            raise ValueError(Booru.error_handling_limit)

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        if block != '':
            self.query = f"{query} -{block}*"

        else:
            self.query = query

        self.specs['tags'] = str(self.query)
        self.specs['limit'] = str(limit)
        self.specs['pid'] = str(page)
        self.specs['json'] = '1'

        try:
            self.data = requests.get(Booru.e926, params=self.specs, headers=Booru.headers)
            self.final = json.loads(better_object(
                self.data.json()), encoding="utf-8")

            self.not_random = parse_image(self.final['posts'])
            shuffle(self.not_random)
            return better_object(self.not_random)

        except Exception as e:
            print(f'Failed to get data: {e}')
