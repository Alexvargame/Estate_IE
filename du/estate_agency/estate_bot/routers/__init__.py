__all__ = ('router',)
from aiogram import Router

from .commands_routers import router as commands_router
from .servey import router as servey_router
from .callback_handlers_routers import router as callback_router
from .servey.handlers_employee_kb import router as employee_kb_router

router = Router(name=__name__)

router.include_routers(
    servey_router,
    employee_kb_router,
    #commands_router,
    callback_router,

)
