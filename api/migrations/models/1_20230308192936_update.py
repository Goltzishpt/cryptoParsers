from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "contract" ADD "cryptocurrency_id" INT NOT NULL;
        ALTER TABLE "contract" ADD CONSTRAINT "fk_contract_cryptocu_3de6a484" FOREIGN KEY ("cryptocurrency_id") REFERENCES "cryptocurrency" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "contract" DROP CONSTRAINT "fk_contract_cryptocu_3de6a484";
        ALTER TABLE "contract" DROP COLUMN "cryptocurrency_id";"""
