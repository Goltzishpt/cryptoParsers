from db_init import Tortoise, connect, register_tortoise, TORTOISE_ORM
from fastapi import FastAPI
import hashlib


app = FastAPI()


@app.on_event("startup")
async def startup():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    register_tortoise(
        app,
        db_url=connect['db_url'],
        modules=connect['modules'],
        generate_schemas=True
    )


@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()


