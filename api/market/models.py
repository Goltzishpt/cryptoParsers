from tortoise import Model, fields


class MarketModel(Model):
    name = fields.CharField(element_type='text', unique=True)
    url = fields.CharField(element_type='text', unique=True)
    cryptocurrency = fields.ReverseRelation["CryptoCurrencyModel"]

    class Meta:
        fields = ('name', 'url')

