from tortoise import Model, fields
from contracts.schemas import ContractsSchemas


class ContractModel(Model):
    name = fields.CharField(max_length=512, null=True)
    contract_address = fields.CharField(max_length=512, null=True)
    chain_id = fields.IntField(null=True)
    decimal = fields.IntField(null=True)
    image = fields.CharField(max_length=512, null=True)
    cryptocurrency = fields.ForeignKeyField("models.CryptoCurrencyModel", on_delete=fields.CASCADE)

    class Meta:
        table = 'contract'

    async def contract_create(self):
        pass

