from scrapy.responsetypes import Response
from crawler.parsers.base import ContractParseBase


class ContractParse(ContractParseBase):
    def __init__(self, response: Response):
        super().__init__(response=response)
        self.response = response

    @property
    def _get_name(self):
        return self.response.xpath('descendant::span/text()').get()

    @property
    def _get_contract_address(self):
        return self.response.xpath('descendant::i/@data-address').get()

    @property
    def _get_chain_id(self):
        return self.response.xpath('descendant::img/@data-chain-id').get()

    @property
    def _get_decimal(self):
        return self.response.xpath('descendant::img/@data-decimals').get()

    @property
    def _get_image(self):
        return self.response.xpath('descendant::img/@src').get()
