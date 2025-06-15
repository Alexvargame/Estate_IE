from aiogram import Router

from .handlers_objects import router as objects_handlers_router


router = Router(name='employee_kb')

router.include_routers(
   objects_handlers_router,
)