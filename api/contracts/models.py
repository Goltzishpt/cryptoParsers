from tortoise import Model, fields
from contracts.schemas import ContractsSchemas


class ContractModel(Model):
    name = fields.CharField(max_length=512, null=True)
    contract_address = fields.CharField(max_length=512, null=True)
    chain_id = fields.IntField(null=True)
    decimal = fields.IntField(null=True)
    image = fields.CharField(max_length=512, null=True)
    cryptocurrency = fields.ForeignKeyField("models.CryptoCurrencyModel", related_name="contracts", on_delete=fields.CASCADE)

    class Meta:
        table = 'contract'

    @classmethod
    async def contract_create(cls, data: ContractsSchemas):
        contracts = cls(
            name=data.name,
            contracts_adress=data.contract_address,
            chain_id=data.chain_id,
            decimal=data.decimal,
            image=data.image,
            cryptocurrency_id=data.cryptocurrency_id
        )

        await contracts.save()
        return contracts

