from aiogram import Router

from .handlers_reg_auth import router as reg_auth_handlers_router


router = Router(name='survey')

router.include_routers(
    reg_auth_handlers_router,
)
