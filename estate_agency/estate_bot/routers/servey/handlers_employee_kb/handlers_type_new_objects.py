from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext


#from estate_agency.estate_bot.db import BotDBClass
# from estate_agency.estate_bot.keyboards.employee_kb.main_employee_kb import EmployeeData, EmployeeDataAction
# from estate_agency.estate_bot.keyboards.employee_kb.type_objects_kb import EmployeeObjectsAction, EmployeeObjects

from estate_bot.keyboards.employee_kb.type_new_object_kb import (build_employee_category_new_object_kb,
                                                                 build_employee_district_new_object_kb,
                                                                 build_employee_repair_state_new_object_kb,
                                                                 build_employee_building_type_new_object_kb,
                                                                 build_employee_save_or_not_new_object_kb)
# from estate_agency.estate_bot.keyboards.employee_kb.main_employee_kb import build_employee_kb


from estate_bot.keyboards.employee_kb.type_new_object_kb import (EmployeeTypeNewObjects, EmployeeTypeNewObjectsAction,
                                                                 EmployeeCategoryNewObjectsAction, EmployeeCategoryNewObjects,
                                                                 EmployeeDistrictNewObjects, EmployeeDistrictNewObjectsAction,
                                                                 EmployeeRepiarStateNewObjects, EmployeeRepairStateNewObjectsAction,
                                                                 EmployeeBuildingTypeNewObjects, EmployeeBuildingTypeNewObjectsAction,
                                                                 EmployeeSaveOrNotNewObjectsAction, EmployeeSaveOrNotStateNewObjects)

from estate_bot.routers.servey.states import OrderNewObject

#BotDB = BotDBClass(Path(__file__).resolve().parent.parent.parent / 'db.sqlite3')

from estate_bot.base_name import BotDB

router = Router(name='employee_type_new_objects')

@router.callback_query(OrderNewObject.waiting_for_type_object)
@router.callback_query(EmployeeTypeNewObjects.filter())
async def get_type_object(clbk: CallbackQuery, callback_data: EmployeeTypeNewObjects, state: FSMContext):
    print('CATEGORY OBJECT')
    await state.update_data(property_type=callback_data.action.value)
    data = await state.get_data()
    await clbk.message.answer(
        text=f"Выберите категорию объекта:",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_category_new_object_kb()
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_category_object)

@router.callback_query(OrderNewObject.waiting_for_category_object)
@router.callback_query(EmployeeCategoryNewObjects.filter())
async def get_category_object(clbk: CallbackQuery, callback_data: EmployeeCategoryNewObjects, state: FSMContext):
    print('DISTRICT OBJECT')
    await state.update_data(property_category=callback_data.action.value)
    data = await state.get_data()
    await clbk.message.answer(
        text=f"Выберите район объекта:",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_district_new_object_kb()
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_district_object)

@router.callback_query(OrderNewObject.waiting_for_district_object)
@router.callback_query(EmployeeDistrictNewObjects.filter())
async def get_distirct_object(clbk: CallbackQuery, callback_data: EmployeeDistrictNewObjects, state: FSMContext):
    print('DISTRICT OBJECT')
    await state.update_data(district=callback_data.action.value)
    data = await state.get_data()
    await clbk.message.answer(
        text=f"Введите адресс:",
        parse_mode=ParseMode.HTML,

    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_address_object)

@router.message(OrderNewObject.waiting_for_address_object)
async def get_address_object(message: types.Message, state: FSMContext):
    print('adress OBJECT')
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Введите кол-во комнат:",
        parse_mode=ParseMode.HTML,

    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_total_area_object)

@router.message(OrderNewObject.waiting_for_total_area_object)
async def get_total_area_object(message: types.Message, state: FSMContext):
    print('area OBJECT')
    await state.update_data(rooms_count=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Введите общую площадь:",
        parse_mode=ParseMode.HTML,

    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_living_area_object)

@router.message(OrderNewObject.waiting_for_living_area_object)
async def get_living_area_object(message: types.Message, state: FSMContext):
    print('area OBJECT')
    await state.update_data(total_area=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Введите жилую площадь:",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_floor_object)

@router.message(OrderNewObject.waiting_for_floor_object)
async def get_floor_object(message: types.Message, state: FSMContext):
    print('area OBJECT')
    await state.update_data(living_area=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Введите этаж:",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_total_floor_object)

@router.message(OrderNewObject.waiting_for_total_floor_object)
async def get_total_floor_object(message: types.Message, state: FSMContext):
    print('area OBJECT')
    await state.update_data(floor=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Введите этажность дома':",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_building_type_object)

@router.message(OrderNewObject.waiting_for_building_type_object)
async def get_building_type_object(message: types.Message, state: FSMContext):
    print('area OBJECT')
    await state.update_data(total_floor=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Выберите тип стен дома':",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_building_type_new_object_kb()
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_repair_state_object)


@router.callback_query(OrderNewObject.waiting_for_repair_state_object)
@router.callback_query(EmployeeBuildingTypeNewObjects.filter())
async def get_repair_state_object(clbk: CallbackQuery, callback_data: EmployeeBuildingTypeNewObjects, state: FSMContext):
    print('area OBJECT')
    await state.update_data(building_type=callback_data.action.value)
    data = await state.get_data()
    await clbk.message.answer(
        text=f"Выберите состояние ремонта в квартире':",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_repair_state_new_object_kb()
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_infrastructure_object)

@router.callback_query(OrderNewObject.waiting_for_infrastructure_object)
@router.callback_query(EmployeeRepiarStateNewObjects.filter())
async def get_infrastructure_object(clbk: CallbackQuery, callback_data: EmployeeRepiarStateNewObjects, state: FSMContext):
    print('RWEPIEOBJECT')
    await state.update_data(repair_state=callback_data.action.value)
    data = await state.get_data()
    await clbk.message.answer(
        text=f"Инфраструктура:",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    print('INFRS', clbk.message.text)
    await state.set_state(OrderNewObject.waiting_for_check_object)

@router.message(OrderNewObject.waiting_for_check_object)
#@router.callback_query(EmployeeSaveOrNotStateNewObjects.filter())
async def get_check_object(message:types.Message, state: FSMContext):
    print('CHECK')
    await state.update_data(infrastructute=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Сохранить?",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_save_or_not_new_object_kb()
    )
    print(data)
    #print(callback_data.action.value)
    await state.set_state(OrderNewObject.waiting_for_save_or_no_object)


@router.callback_query(OrderNewObject.waiting_for_check_object)
@router.callback_query(EmployeeSaveOrNotStateNewObjects.filter())
async def get_save_or_no_object(clbk: CallbackQuery, callback_data: EmployeeSaveOrNotStateNewObjects, state: FSMContext):
    print('save_OR_NO')
    #await state.update_data(infrastructute=message.text)
    data = await state.get_data()
    # await clbk.message.answer(
    #     text=f"Сохранить?",
    #     parse_mode=ParseMode.HTML,
    #     reply_markup=build_employee_save_or_not_new_object_kb()
    # )
    print(callback_data.action.value)
    if callback_data.action.value == 'Да':
        print('Save')
        for key, value in data.items():
            print(key, value)
    else:
        print('Not Save')
    #await state.set_state(OrderNewObject.waiting_for_repair_state_object)

# @router.callback_query(EmployeeData.filter(F.action == EmployeeDataAction.objects))
# async def get_type_object(clbk: CallbackQuery, state: FSMContext):
#     print("Objects")
#
#     await clbk.message.answer(
#
#         text=f"Выберите тип объекта:",
#         parse_mode=ParseMode.HTML,
#         reply_markup=build_employee_type_objects_kb(),
#     )
#     print('CLBKMESSAGE', clbk.message)
#     await state.set_state(OrderEmployeeObjects.waiting_for_type_object)
#
# @router.callback_query(EmployeeObjects.filter(F.action == EmployeeObjectsAction.add_new))
# async def add_new_object(clbk: CallbackQuery, state: FSMContext):
#     print('New object')
#     await clbk.message.answer(
#
#         text=f"Выберите тип объекта:",
#         parse_mode=ParseMode.HTML,
#         #reply_markup=build_employee_type_objects_kb(), клавиатура стипами объектов,  потом уже новый хенжлер
#     )



# @router.callback_query(EmployeeObjects.filter(F.action == EmployeeObjectsAction.flats))
# async def get_flats(clbk:CallbackQuery, state:FSMContext):
#     print('all flats')
#     print('clbk.message.from_user.id', clbk.message.from_user.id)
#     print(clbk.message.chat.id)
#     flats = BotDB.get_all_flats_for_user(clbk.message.chat.id)
#     t1 = f"Все квартиры\n"
#     t2 = ''
#     for flat in flats:
#         t2 += f"{flat[1]} - цена {flat[3]}\n"
#     output_text = t1 +t2
#     await clbk.message.answer(
#             text=output_text,
#             parse_mode=ParseMode.HTML,
#             #reply_markup=build_employee_type_objects_kb(),
#         )
#
# @router.callback_query(EmployeeObjects.filter(F.action == EmployeeObjectsAction.cancel))
# async def cancel_objects_kb(clbk:CallbackQuery, state:FSMContext):
#     await clbk.message.answer(
#         text=f"Выберите действие в меню",
#         reply_markup=build_employee_kb()
#     )