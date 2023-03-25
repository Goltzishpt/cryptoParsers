from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


db_url = "postgres://user:admin@127.0.0.1:5432/postgres"

TORTOISE_ORM = {
    "connections": {
        "default": db_url
    },
    "apps": {
        "models": {
            "models": [
                "cryptocurrency.models",
                "contracts.models",
                "aerich.models",
            ],
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


def setup_database(app: FastAPI):
    register_tortoise(
        app,
        **connect
    )
