from aiogram import Router

from .handlers_objects import router as objects_handlers_router
from .handlers_type_new_objects import router as type_new_objects_handlers_router
from .handlers_flats import router as flats_router


router = Router(name='employee_kb')

router.include_routers(
   objects_handlers_router,
   type_new_objects_handlers_router,
   flats_router,
)