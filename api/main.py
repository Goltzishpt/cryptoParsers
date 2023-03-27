import uvicorn
from utils.db_init import setup_database
from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup():
    setup_database(app)


@app.on_event("shutdown")
async def shutdown():
    pass


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=5006,
        reload=True
    )
