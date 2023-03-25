from scrapy.responsetypes import Response
from crawler.parsers.base import TagParseBase


class TagParse(TagParseBase):
    def __init__(self, response: Response):
        super().__init__(response=response)
        self.response = response

    @property
    def _get_name(self):
        return self.response.xpath('descendant::node()').get()

    @property
    def _get_link(self):
        return f"https://www.coingecko.com{self.response.xpath('descendant-or-self::node()/@href').get()}"