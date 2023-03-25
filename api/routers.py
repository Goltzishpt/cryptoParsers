from fastapi import APIRouter
from loader import app

router = APIRouter()


@router.get('/item')
def get_item():
    return {'item': 'value'}


@router.post('/item')
def get_item():
    return {'item': 'value'}


app.include_router(router)
