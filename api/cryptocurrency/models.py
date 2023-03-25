from tortoise import Model, fields
from tortoise.contrib.postgres.fields import ArrayField
from cryptocurrency.schemas import CryptoCurrencySchemas


class CryptoCurrencyModel(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=512, null=True)
    rank = fields.IntField(null=True)
    symbol = fields.CharField(max_length=512, null=True)
    url = fields.CharField(max_length=512, null=True)
    # contracts = fields.ForeignKeyField('models.ContractModel', null=True, on_delete=fields.CASCADE)
    image = fields.CharField(max_length=512, null=True)
    explorers = ArrayField(element_type='text', null=True)
    wallets = ArrayField(element_type='text', null=True)
    community = ArrayField(element_type='text', null=True)
    tags = ArrayField(element_type='text', null=True)

    class Meta:
        table = 'cryptocurrency'

    async def cryptocurrency_create(self):
        pass
