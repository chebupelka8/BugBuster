from fastapi import APIRouter

from .routers import challenges_router, users_router


__all__ = ["router"]


router = APIRouter(
    prefix="/api/v1",
    tags=["APIv1"]
)

router.include_router(challenges_router)
router.include_router(users_router)
