from db_init import setup_database
from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup():
    setup_database(app)


@app.on_event("shutdown")
async def shutdown():
    pass


