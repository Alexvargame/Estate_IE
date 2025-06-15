from aiogram import Router

from .start_auth_kb_router import router as start_auth_kb_router

router = Router(name=__name__)

router.include_routers(
    start_auth_kb_router,
)