from tortoise import Model, fields


class MarketModel(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=64, element_type='text', unique=True)
    url = fields.CharField(max_length=512, element_type='text', unique=True)
    cryptocurrency = fields.ReverseRelation["CryptoCurrencyModel"]

    class Meta:
        table = 'market'


    # @classmethod
    # async def market_create(cls, data: MarketSchemas):
    #     market = cls(
    #         id=data.id,
    #         name=data.name,
    #         url=data.url,
    #         cryptocurrency_id=data.cryptocurrency_id
    #     )
    #
    #     await market.save()
    #     return market
