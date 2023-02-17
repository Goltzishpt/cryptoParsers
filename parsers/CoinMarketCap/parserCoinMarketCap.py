import json
from scrapy.responsetypes import Response
from crawler.parsers.base import CryptoCurrencyParseBase
from crawler.parsers.CoinMarketCap.tagParser import TagParse
from crawler.parsers.CoinMarketCap.contractParser import ContractParse


class CryptoCurrencyCoinMarketCapParse(CryptoCurrencyParseBase):

    def __init__(self, response: Response):
        super().__init__(response=response)
        self.response = response
        self.data = json.loads(self.response.text)['data']

    @property
    def id(self):
        return self.data['id']

    @property
    def _get_url(self):
        slug_crypto = self.data['slug']
        return f'https://coinmarketcap.com/currencies/{slug_crypto}/'

    @property
    def _get_name(self):
        return self.data['name']

    @property
    def _get_image(self):
        return f'https://s2.coinmarketcap.com/static/img/coins/64x64/{self.id}.png'

    @property
    def _get_symbol(self):
        return self.data['symbol']

    @property
    def _get_rank(self):
        return self.data['statistics']['rank']

    @property
    def _get_website(self):
        return self.data['urls']['website']

    @property
    def _get_explorers(self):
        return self.data['urls']['explorer']

    @property
    def _get_wallets(self):
        return self.data['wallets']

    @property
    def _get_community(self):
        return {
            'chat': self.data['urls']['chat'],
            'reddit': self.data['urls']['reddit'],
            'facebook': self.data['urls']['facebook'],
            'twitter': self.data['urls']['twitter']
        }

    @property
    def _get_api_id(self):
        return self.id

    @property
    def _get_contracts(self):
        if 'platforms' in self.data.keys():
            return [ContractParse(response=item).get_item() for item in self.data['platforms']]

    @property
    def _get_tags(self):
        return [TagParse(response=item).get_item() for item in self.data['tags']]
