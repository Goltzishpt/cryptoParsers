from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise, run_async
from api.cryptocurrency.models import CryptoCurrencyModel
from settings import config
from tortoise.exceptions import IntegrityError


TORTOISE_ORM = {
    "connections": {
        "default": config.db_uri
    },
    "apps": {
        "models": {
            "models": ["cryptocurrency.models", "contracts.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC"
}


connect = {
    "db_url": config.db_uri,
    "modules": {
        "models": [
            "cryptocurrency.models",
            "contracts.models",
        ],
    },
    "generate_schemas": True,
    "add_exception_handlers": True,
}


def setup_database(app: FastAPI):
    register_tortoise(
        app,
        **connect
    )


