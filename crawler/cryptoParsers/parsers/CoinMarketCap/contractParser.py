import json
from scrapy.responsetypes import Response
from crawler.parsers.base import ContractParseBase


class ContractParse(ContractParseBase):
    def __init__(self, response: Response):
        super().__init__(response=response)
        self.response = response

    @property
    def _get_name(self):
        return self.response['contractPlatform']

    @property
    def _get_contract_address(self):
        return self.response['contractAddress']

    @property
    def _get_chain_id(self):
        return self.response['contractChainId']

    @property
    def _get_decimal(self):
        if 'contractDecimals' in self.response.keys():
            return self.response['contractDecimals']

    @property
    def _get_image(self):
        return f'https://s2.coinmarketcap.com/static/img/coins/64x64/{self.response["contractId"]}.png'



