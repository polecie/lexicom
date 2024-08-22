from fastapi import APIRouter, Depends, HTTPException, Query, Response
from pydantic import ValidationError

from src.api.v1.schemas import Address, Phone, RequestData
from src.db.cache import AbstractCache, get_cache

router = APIRouter()


@router.get(
    path="/check_data",
    tags=["bad"],
    response_model=Address,
    status_code=200,
)
async def check(phone: str = Query(), cache: AbstractCache = Depends(get_cache)):  # ’89090000000’
    """
    Плохой пример ручки для проверки данных, не рестфул, но по тз
    """
    try:
        phone = Phone(phone=phone).phone
    except ValidationError:
        raise HTTPException(status_code=400)
    if address := await cache.get(phone):
        return Address(address=address)
    raise HTTPException(status_code=404)


@router.post(
    path="/write_data",
    tags=["bad"],
    response_model=None,
    status_code=201,
    responses={
        201: {"description": "Created", "content": None},
        204: {"description": "No Content", "content": None},
    },
)
async def write(content: RequestData, cache: AbstractCache = Depends(get_cache)):
    """
    Плохой пример ручки для добавления/обновления данных, не рестфул, но по тз
    """
    cached = await cache.get(content.phone)
    status_code = 204 if cached else 201
    await cache.set(name=content.phone, value=content.address)
    return Response(status_code=status_code)
