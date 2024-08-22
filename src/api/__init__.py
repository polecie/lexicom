from fastapi import APIRouter

from src.api.v1.resources import router as __v1_endpoints__

__all__ = [
    "router",
]

router = APIRouter(prefix="/api/v1")


router.include_router(__v1_endpoints__)
