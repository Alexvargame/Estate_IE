from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext


#from estate_agency.estate_bot.db import BotDBClass
from estate_bot.keyboards.employee_kb.main_employee_kb import EmployeeData, EmployeeDataAction
from estate_bot.keyboards.employee_kb.type_objects_kb import EmployeeObjectsAction, EmployeeObjects

from estate_bot.keyboards.employee_kb.type_objects_kb import build_employee_type_objects_kb
from estate_bot.keyboards.employee_kb.type_new_object_kb import build_employee_type_new_object_kb
from estate_bot.keyboards.employee_kb.main_employee_kb import build_employee_kb
from estate_bot.keyboards.employee_kb.flats_kb import build_flats_kb

from estate_bot.routers.servey.states import OrderEmployeeObjects, OrderNewObject


#BotDB = BotDBClass(Path(__file__).resolve().parent.parent.parent / 'db.sqlite3')

from estate_bot.base_name import BotDB

router = Router(name='employee_objects')


#Нужен ли тут state?
@router.callback_query(EmployeeData.filter(F.action == EmployeeDataAction.objects))
async def get_main_menu_item(clbk: CallbackQuery, state: FSMContext):
    print(clbk.data)

    await clbk.message.answer(

        text=f"Выберите тип объекта:",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_type_objects_kb(),
    )
    print('CLBKMESSAGE', clbk.message)
    await state.set_state(OrderEmployeeObjects.waiting_for_type_object)

@router.callback_query(EmployeeObjects.filter(F.action == EmployeeObjectsAction.add_new))
async def add_new_object(clbk: CallbackQuery, state: FSMContext):
    print('New object')
    await clbk.message.delete()
    await clbk.message.answer(
        text=f"Выберите тип объекта:",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_type_new_object_kb()
    )
    await state.set_state(OrderNewObject.waiting_for_type_object)
    #await state.update_data(property_type=E)
    # print('message text', clbk.message.reply_markup.inline_keyboard)
    # data = await state.get_data()
    # print('state', data)

@router.callback_query(EmployeeObjects.filter(F.action == EmployeeObjectsAction.flats))
async def get_flats(clbk:CallbackQuery, state:FSMContext):

    await clbk.message.answer(
        text='Выберите пункт меню',
        parse_mode=ParseMode.HTML,
        reply_markup=build_flats_kb(),
    )
    await state.set_state(OrderEmployeeObjects.waiting_for_choice_flats_menu)


@router.callback_query(EmployeeObjects.filter(F.action == EmployeeObjectsAction.cancel))
async def cancel_objects_kb(clbk:CallbackQuery, state:FSMContext):
    await clbk.message.answer(
        text=f"Выберите действие в меню",
        reply_markup=build_employee_kb()
    )