from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise, run_async
from api.cryptocurrency.models import CryptoCurrencyModel
from config import DB_NAME, DB_PORT, DB_HOST, POSTGRES_USER, POSTGRES_PASSWORD
from tortoise.exceptions import IntegrityError


db_url = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


TORTOISE_ORM = {
    "connections": {
        "default": db_url
    },
    "apps": {
        "models": {
            "models": ["api.cryptocurrency.models", "contracts.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC"
}


connect = {
    "db_url": db_url,
    "modules": {
        "models": [
            "cryptocurrency.models",
            "contracts.models",
        ],
    },
    "generate_schemas": True,
    "add_exception_handlers": True,
}


async def test_db_connection():
    try:
        await Tortoise.init(
            db_url=db_url,
            modules={'modules': ['api.cryptocurrency.models']}
        )
        await Tortoise.generate_schemas()
        result = await CryptoCurrencyModel.filter(some_field='some_value').first()
        print(result)
    except IntegrityError as e:
        print(f"Failed to connect to the database: {e}")

if __name__ == '__main__':
    run_async(test_db_connection())
