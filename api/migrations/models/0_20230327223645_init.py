from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "market" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL UNIQUE,
    "url" VARCHAR(512) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "cryptocurrency" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(512),
    "rank" INT,
    "symbol" VARCHAR(512),
    "url" VARCHAR(512),
    "image" VARCHAR(512),
    "explorers" text[],
    "wallets" text[],
    "community" text[],
    "tags" text[],
    "market_id" INT NOT NULL REFERENCES "market" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_cryptocurre_name_833cd1" UNIQUE ("name", "symbol", "market_id")
);
CREATE TABLE IF NOT EXISTS "contract" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(512),
    "contract_address" VARCHAR(512),
    "chain_id" INT,
    "decimal" INT,
    "image" VARCHAR(512),
    "cryptocurrency_id" INT NOT NULL REFERENCES "cryptocurrency" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
