from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext


#from estate_agency.estate_bot.db import BotDBClass
from estate_agency.estate_bot.keyboards.employee_kb.main_employee_kb import EmployeeData, EmployeeDataAction

from estate_agency.estate_bot.keyboards.employee_kb.type_objects_kb import build_employee_type_objects_kb

from estate_agency.estate_bot.routers.servey.states import OrderEmployeeObjects

#BotDB = BotDBClass(Path(__file__).resolve().parent.parent.parent / 'db.sqlite3')

from estate_agency.estate_bot.base_name import BotDB

router = Router(name='employee_objects')

@router.callback_query(EmployeeData.filter(F.action == EmployeeDataAction.objects))
async def get_type_object(clbk: CallbackQuery, state: FSMContext):
    print("Objects")

    await clbk.message.answer(

        text=f"Выберите тип объекта:",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_type_objects_kb(),
    )
    print('CLBKMESSAGE', clbk.message)
    await state.set_state(OrderEmployeeObjects.waiting_for_type_object)


