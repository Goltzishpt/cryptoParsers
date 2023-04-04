from fastapi import APIRouter
from main import app

router = APIRouter()


@router.get('/')
def get_item():
    return {'item': 'value'}


@router.post('/item')
def get_item():
    return {'item': 'value'}


app.include_router(router)
