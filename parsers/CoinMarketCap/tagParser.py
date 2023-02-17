import json
from scrapy.responsetypes import Response
from crawler.parsers.base import TagParseBase


class TagParse(TagParseBase):

    def __init__(self, response: Response):
        super().__init__(response=response)
        self.response = response

    @property
    def _get_name(self):
        return self.response['name']

    @property
    def _get_link(self):
        return f'https://coinmarketcap.com/view/{self.response["slug"]}'
