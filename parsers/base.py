from scrapy.responsetypes import Response


class ParseBase:
    fields = ()

    def __init__(self, response: Response):
        self.response = response

    def get_item(self):
        item = dict()
        for i in self.fields:
            # print(i, '--------------------',  f'_get_{i}', '---------', getattr(self, f'_get_{i}'))
            item[i] = getattr(self, f'_get_{i}')
        return item


class ContractParseBase(ParseBase):
    fields = ('name', 'contract_address', 'chain_id', 'decimal', 'image')

    def __init__(self, response: Response):
        super().__init__(response)


class CryptoCurrencyParseBase(ParseBase):
    fields = ('url', 'name', 'contracts', 'image', 'symbol', 'rank', 'explorers', 'wallets', 'community', 'api_id',
              'tags')

    def __init__(self, response: Response):
        super().__init__(response)


class TagParseBase(ParseBase):
    fields = ('name', 'link')

    def __init__(self, response: Response):
        super().__init__(response)
