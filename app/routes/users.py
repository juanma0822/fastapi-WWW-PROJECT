from fastapi import APIRouter
from app.controllers.users_controller import router as users_controller_router

router = APIRouter()
router.include_router(users_controller_router, prefix="/users", tags=["Users"])