from asgiref.sync import sync_to_async

from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from estate_bot.validators.validators_for_create_new_object import (validator_for_rooms_count,
                                                                    validator_for_total_area,
                                                                    validator_for_living_area,
                                                                    validator_for_floor,
                                                                    validator_for_total_floor,
                                                                    validator_for_price,
                                                                    validator_for_text_filed)

from estate_agency.estate_agency_apps.property.services import (PropertyTypeService, PropertyCategoryService,
                                                                DistrictService, BuildingTypeService,
                                                                RepairStateService, PropertyService,CityService)
from estate_agency.estate_agency_apps.property.repository import (PropertyTypeRepository, PropertyCategoryRepository,
                                                                DistrictRepository, RepairStateRepository,
                                                                BuildingTypeRepository, PropertyRepository,
                                                                CityRepository
                                                                )

from estate_bot.keyboards.employee_kb.type_new_object_kb import (build_employee_type_new_object_kb,
                                                                 build_employee_category_new_object_kb,
                                                                 build_employee_district_new_object_kb,
                                                                 build_employee_repair_state_new_object_kb,
                                                                 build_employee_building_type_new_object_kb,
                                                                 build_employee_save_or_not_new_object_kb,
                                                                 build_update_new_object_kb)
from estate_bot.keyboards.employee_kb.type_objects_kb import build_employee_type_objects_kb


from estate_bot.keyboards.employee_kb.type_new_object_kb import (EmployeeTypeNewObjects, EmployeeTypeNewObjectsAction,
                                                                 EmployeeCategoryNewObjectsAction, EmployeeCategoryNewObjects,
                                                                 EmployeeDistrictNewObjects, EmployeeDistrictNewObjectsAction,
                                                                 EmployeeRepiarStateNewObjects, EmployeeRepairStateNewObjectsAction,
                                                                 EmployeeBuildingTypeNewObjects, EmployeeBuildingTypeNewObjectsAction,
                                                                 EmployeeSaveOrNotNewObjectsAction, EmployeeSaveOrNotStateNewObjects,
                                                                 EmployeeUpdateObject, EmployeeUpdateObjectAction)

from estate_bot.keyboards.employee_kb.main_employee_kb import build_employee_kb

from estate_bot.routers.servey.states import OrderNewObject
from estate_bot.dictionaries import get_dictionary_object

from estate_agency.estate_agency_apps.dtos.property.request_dto import CreatePropertyDTO
from estate_agency.estate_agency_apps.users.models import BaseUser
#BotDB = BotDBClass(Path(__file__).resolve().parent.parent.parent / 'db.sqlite3')

from estate_bot.base_name import BotDB

router = Router(name='employee_type_new_objects')

DICT_OBJECT = get_dictionary_object()
@sync_to_async
def create_property_sync(data):
    return PropertyService(PropertyRepository()).create_object(data)
@sync_to_async
def create_repair_state_sync(data):
    return RepairStateService(RepairStateRepository()).get_object_by_transcription(data)
@sync_to_async
def create_property_type_sync(data):
    return PropertyTypeService(PropertyTypeRepository()).get_object_by_transcription(data)
@sync_to_async
def create_property_category_sync(data):
    return PropertyCategoryService(PropertyCategoryRepository()).get_object_by_transcription(data)
@sync_to_async
def create_district_sync(data):
    return DistrictService(DistrictRepository()).get_object_by_transcription(data)
@sync_to_async
def create_building_type_sync(data):
    return BuildingTypeService(BuildingTypeRepository()).get_object_by_transcription(data)
# @sync_to_async
# def create_city_sync(data):
#     return CityService(CityRepository()).get_object_by_name(data)

@sync_to_async
def create_user_sync(data):
    print('create_user-data')
    return BaseUser.objects.get(id=data)


def output_data_to_screen(data):
    title = 'Новый объект\n'
    output_data_to_screen = ''
    for key, value in data.items():
        output_data_to_screen += f'{DICT_OBJECT[key]}: {value}\n'
    return title + output_data_to_screen



@router.callback_query(OrderNewObject.waiting_for_type_object)
@router.callback_query(EmployeeTypeNewObjects.filter())
async def get_type_object(clbk: CallbackQuery, callback_data: EmployeeTypeNewObjects, state: FSMContext):
    print('CATEGORY OBJECT', callback_data, callback_data.action.name)
    await clbk.message.delete()
    if callback_data.action.name == 'cancel':
        await clbk.message.answer(
            text=f"Выберите тип объекта:",
            parse_mode=ParseMode.HTML,
            reply_markup=build_employee_type_objects_kb()
        )
    else:
        tmp = await create_property_type_sync(callback_data.action.name)
        await state.update_data(property_type=tmp)
        data = await state.get_data()
        await clbk.message.answer(
            text=output_data_to_screen(data),
            parse_mode=ParseMode.HTML,
        )
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
    clbk.message.delete()
    if callback_data.action.name == 'cancel':
        await clbk.message.answer(
            text=f"Выберите категорию объекта:",
            parse_mode=ParseMode.HTML,
            reply_markup=build_employee_type_new_object_kb()
        )
    else:
        tmp = await create_property_category_sync(callback_data.action.name)
        await state.update_data(property_category=tmp)
        data = await state.get_data()
        await clbk.message.answer(
            text=output_data_to_screen(data),
            parse_mode=ParseMode.HTML,
        )
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
    clbk.message.delete()
    if callback_data.action.name == 'cancel':
        await clbk.message.answer(
            text=f"Выберите район объекта:",
            parse_mode=ParseMode.HTML,
            reply_markup=build_employee_category_new_object_kb()
        )
    else:
        tmp = await create_district_sync(callback_data.action.name)
        await state.update_data(district=tmp)
        data = await state.get_data()
        await clbk.message.answer(
            text=output_data_to_screen(data),
            parse_mode=ParseMode.HTML,
        )
        await clbk.message.answer(
            text=f"Введите адрес:",
            parse_mode=ParseMode.HTML,

        )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_address_object)

@router.message(OrderNewObject.waiting_for_address_object)
async def get_address_object(message: types.Message, state: FSMContext):
    print('adress OBJECT')
    message.delete()
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Введите кол-во комнат:",
        parse_mode=ParseMode.HTML,

    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_rooms_count_object)



@router.message(OrderNewObject.waiting_for_rooms_count_object)
async def get_total_area_object(message: types.Message, state: FSMContext):
    print('ROOMSCOUNT OBJECT')
    message.delete()
    rooms = await validator_for_rooms_count(message)
    if rooms is None:
        return
    await state.update_data(rooms_count=rooms)
    data = await state.get_data()
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Введите общую площадь:",
        parse_mode=ParseMode.HTML,

    )
    print(message.text, 'ROOMS', data)
    await state.set_state(OrderNewObject.waiting_for_total_area_object)


@router.message(OrderNewObject.waiting_for_total_area_object)
async def get_living_area_object(message: types.Message, state: FSMContext):
    print('area OBJECT')
    message.delete()
    total_area = await validator_for_total_area(message)
    if total_area is None:
        return
    await state.update_data(total_area=total_area)
    data = await state.get_data()
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Введите жилую площадь:",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_living_area_object)

@router.message(OrderNewObject.waiting_for_living_area_object)
async def get_floor_object(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print('area OBJECT')
    message.delete()
    living_area = await validator_for_living_area(message, data['total_area'])
    if living_area is None:
        return
    await state.update_data(living_area=living_area)
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Введите этажность дома:",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_total_floor_object)

@router.message(OrderNewObject.waiting_for_total_floor_object)
async def get_total_floor_object(message: types.Message, state: FSMContext):
    print('area OBJECT')
    message.delete()
    total_floor = await validator_for_total_area(message)
    if total_floor is None:
        return
    await state.update_data(total_floor=total_floor)
    data = await state.get_data()
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Введите этаж:",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_floor_object)

@router.message(OrderNewObject.waiting_for_floor_object)
async def get_building_type_object(message: types.Message, state: FSMContext):
    print('area OBJECT')
    message.delete()
    data = await state.get_data()
    floor = await validator_for_floor(message, data['total_floor'])
    if floor is None:
        return
    await state.update_data(floor=floor)
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Выберите тип стен дома':",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_building_type_new_object_kb()
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_building_type_object)


@router.callback_query(OrderNewObject.waiting_for_building_type_object)
@router.callback_query(EmployeeBuildingTypeNewObjects.filter())
async def get_repair_state_object(clbk: CallbackQuery, callback_data: EmployeeBuildingTypeNewObjects, state: FSMContext):
    print('area OBJECT')
    clbk.message.delete()
    tmp = await create_building_type_sync(callback_data.action.name)
    await state.update_data(building_type=tmp)
    data = await state.get_data()
    await clbk.message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await clbk.message.answer(
        text=f"Выберите состояние ремонта в квартире:",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_repair_state_new_object_kb()
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_repair_state_object)

@router.callback_query(OrderNewObject.waiting_for_repair_state_object)
@router.callback_query(EmployeeRepiarStateNewObjects.filter())
async def get_infrastructure_object(clbk: CallbackQuery, callback_data: EmployeeRepiarStateNewObjects, state: FSMContext):
    print('RWEPIEOBJECT')
    clbk.message.delete()
    if callback_data.action.name == 'cancel':
        await clbk.message.answer(
            text=f"Выберите тип стен дома':",
            parse_mode=ParseMode.HTML,
            reply_markup=build_employee_building_type_new_object_kb()
        )
    else:
        tmp = await create_repair_state_sync(callback_data.action.name)
        await state.update_data(repair_state=tmp)
        data = await state.get_data()
        await clbk.message.answer(
            text=output_data_to_screen(data),
            parse_mode=ParseMode.HTML,
        )
        await clbk.message.answer(
            text=f"Инфраструктура:",
            parse_mode=ParseMode.HTML,
        )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_infrastructure_object)

@router.message(OrderNewObject.waiting_for_infrastructure_object)
async def get_building_type_object(message: types.Message, state: FSMContext):
    print('price OBJECT')
    infrastructure = await validator_for_text_filed(message)
    if infrastructure is None:
        return
    await state.update_data(infrastructure=infrastructure)
    data = await state.get_data()
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Введите описание объекта':",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_discription_object)

@router.message(OrderNewObject.waiting_for_discription_object)
async def get_building_type_object(message: types.Message, state: FSMContext):
    print('price OBJECT')
    description = await validator_for_text_filed(message)
    if description is None:
        return
    await state.update_data(description=description)
    data = await state.get_data()
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Введите титул объявления':",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_title_object)
@router.message(OrderNewObject.waiting_for_title_object)
async def get_building_type_object(message: types.Message, state: FSMContext):
    print('price OBJECT')
    await state.update_data(title=message.text)
    data = await state.get_data()
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Введите цену объекта':",
        parse_mode=ParseMode.HTML,
    )
    print(data)
    await state.set_state(OrderNewObject.waiting_for_price_object)
@router.message(OrderNewObject.waiting_for_price_object)
#@router.callback_query(EmployeeSaveOrNotStateNewObjects.filter())
async def get_price_object(message:types.Message, state: FSMContext):
    print('CHECK')
    price = await validator_for_price(message)
    if price is None:
        return
    await state.update_data(price=price)
    data = await state.get_data()
    await message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=f"Сохранить?",
        parse_mode=ParseMode.HTML,
        reply_markup=build_employee_save_or_not_new_object_kb()
    )
    print(data)

    await state.set_state(OrderNewObject.waiting_for_save_or_no_object)

# @router.callback_query(OrderNewObject.waiting_for_save_or_no_object)
# async def handle_waiting_for_save(clbk: CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     await clbk.message.answer(
#         text='Если Вы все указали правильно, нажмите "Да", чтобы сохранить объявление\n'
#              'Если нет, выберите "Исправить"',
#     )
#     await clbk.message.answer(
#         text=output_data_to_screen(data),
#         parse_mode=ParseMode.HTML,
#     )
#@router.callback_query(OrderNewObject.waiting_for_save_or_no_object)
@router.callback_query(EmployeeSaveOrNotStateNewObjects.filter(),
                       StateFilter(OrderNewObject.waiting_for_save_or_no_object))
async def get_save_or_no_object(clbk: CallbackQuery, callback_data: EmployeeSaveOrNotStateNewObjects,
                                state: FSMContext):
    data = await state.get_data()
    data.pop('field_to_edit', None)
    await clbk.message.answer(
        text='Если Вы все указали правильно, нажмите "Да", чтобы сохранить объявление\n'
             'Если нет, выберите "Исправить"',
    )
    await clbk.message.answer(
        text=output_data_to_screen(data),
        parse_mode=ParseMode.HTML,
    )
    if callback_data.action.name == 'yes':
        print('Save')
        user = await create_user_sync(BotDB.get_user(user_bot_id=clbk.from_user.id))
        dataDTO = CreatePropertyDTO(
            **data,
            is_active=1,
            employee=user,
        )
        new_property = await create_property_sync(dataDTO)
        await message.bot.send_message(message.from_user.id,
                                       f"{message.from_user.first_name}. Выберите действие в меню",
                                       reply_markup=build_employee_kb()
        )
    elif callback_data.action.name == 'update':
        print('UUIPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
        await clbk.message.answer(
            text='Выберите, что вы хотите исправить',
            parse_mode=ParseMode.HTML,
            reply_markup=build_update_new_object_kb(),
        )
    await state.set_state(OrderNewObject.waiting_for_edit_object)

#@router.callback_query(OrderNewObject.waiting_for_edit_object)
@router.callback_query(EmployeeUpdateObject.filter(),
                       StateFilter(OrderNewObject.waiting_for_edit_object)
                       )
async def update_object(clbk: CallbackQuery,
                        callback_data: EmployeeUpdateObject,#(action = EmployeeUpdateObjectAction.value),
                        state: FSMContext):
    data = await state.get_data()
    await clbk.message.answer(
        text='Введите правильные данные"'
    )
    print(callback_data.action.name)
    await state.update_data(field_to_edit=callback_data.action.name)
    await state.set_state(OrderNewObject.waiting_for_correct_data_object)

@router.message(OrderNewObject.waiting_for_correct_data_object)
async def correct_data_object(message: types.Message, state: FSMContext):
    data = await state.get_data()
    corr_field = data.get('field_to_edit')
    if not corr_field:
        await message.answer("Ошибка: не найдено, какое поле редактируется.")
        return
    await state.update_data({corr_field: message.text})
    await message.answer("Данные обновлены.")
    await message.answer(
        text='Если Вы все указали правильно, нажмите "Да", чтобы сохранить объявление\n'
             'Если нет, выберите, что исправить.',
        reply_markup=build_employee_save_or_not_new_object_kb()
    )
    await state.set_state(OrderNewObject.waiting_for_save_or_no_object)
