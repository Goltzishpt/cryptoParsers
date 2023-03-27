from tortoise import Model, fields
from tortoise.contrib.postgres.fields import ArrayField
from cryptocurrency.schemas import CryptoCurrencySchemas


class CryptoCurrencyModel(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=512, null=True)
    rank = fields.IntField(null=True)
    symbol = fields.CharField(max_length=512, null=True)
    url = fields.CharField(max_length=512, null=True)
    contracts = fields.ReverseRelation["ContractModel"]
    image = fields.CharField(max_length=512, null=True)
    explorers = ArrayField(element_type='text', null=True)
    wallets = ArrayField(element_type='text', null=True)
    community = ArrayField(element_type='text', null=True)
    tags = ArrayField(element_type='text', null=True)

    class Meta:
        table = 'cryptocurrency'

    @classmethod
    async def cryptocurrency_create(cls, data: CryptoCurrencySchemas):
        cryptocurrency = cls(
            id=data.api_id,
            name=data.name,
            rank=data.rank,
            symbol=data.symbol,
            url=data.url,
            contracts=data.contracts,
            image=data.image,
            explorers=data.explorers,
            wallets=data.wallets,
            community=data.community,
            tags=data.tags
        )
        await cryptocurrency.save()
        return cryptocurrency
