from enum import Enum
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,)
from aiogram.filters.callback_data import CallbackData

from estate_agency.estate_agency_apps.property.services import PropertyTypeService, PropertyCategoryService
from estate_agency.estate_agency_apps.property.repository import PropertyTypeRepository, PropertyCategoryRepository


def create_enum_from_data(enum_name, data):
    print(data)
    enum_members = {item.transcription: item.name for item in data}
    enum_members['cancel'] = 'Отмена'
    print('ENMEM',enum_members)
    return Enum(enum_name, enum_members)

# Используем:
EmployeeTypeNewObjectsAction = create_enum_from_data("EmployeeTypeNewObjectsAction",
                                                     PropertyTypeService(PropertyTypeRepository()).list_objects())
# class EmployeeTypeNewObjectsAction(Enum):
#
#     # def __init__(self, data):
#     #     self.object_dict = dict.fromkeys([pr.transcrtiption for pr in data])
#     #     for d in data:
#     #         self.object_dict[d.transcription] = d.name
#     #         print(self.object_dict)
#     flat = 'Квартира'
#     house = 'Дом'
#     cancel = 'Отмена'

class EmployeeTypeNewObjects(CallbackData, prefix='employee_type_new_objects'):
    action: EmployeeTypeNewObjectsAction

# class EmployeeCategoryNewObjectsAction(Enum):
#     # def __init__(self, data):
#     #     for d in data:
#     #         print(d.__name__)
#     living = 'Жилая'
#     prom = 'Промышленная'
#     cancel = 'Отмена'
#     society = 'Общественная'
EmployeeCategoryNewObjectsAction = create_enum_from_data('EmployeeCategoryNewObjectsAction',
                                                         PropertyCategoryService(PropertyCategoryRepository()).list_objects())
class EmployeeCategoryNewObjects(CallbackData, prefix='employee_category_new_objects'):
    action: EmployeeCategoryNewObjectsAction

class EmployeeDistrictNewObjectsAction(Enum):
    # def __init__(self, data):
    #     for d in data:
    #         print(d.__name__)
    gsv = 'ГСВ'
    cancel = 'Отмена'
class EmployeeDistrictNewObjects(CallbackData, prefix='employee_district_new_objects'):
    action: EmployeeDistrictNewObjectsAction

class EmployeeBuildingTypeNewObjectsAction(Enum):
    # def __init__(self, data):
    #     for d in data:
    #         print(d.__name__)
    brick = 'Кирпич'
    cancel = 'Отмена'
class EmployeeBuildingTypeNewObjects(CallbackData, prefix='employee_building_type_new_objects'):
    action: EmployeeBuildingTypeNewObjectsAction

class EmployeeRepairStateNewObjectsAction(Enum):
    # def __init__(self, data):
    #     for d in data:
    #         print(d.__name__)
    euro = 'Евроремонт'
    cancel = 'Отмена'
class EmployeeRepiarStateNewObjects(CallbackData, prefix='employee_repair_state_new_objects'):
    action: EmployeeRepairStateNewObjectsAction

class EmployeeSaveOrNotNewObjectsAction(Enum):
    # def __init__(self, data):
    #     for d in data:
    #         print(d.__name__)
    yes = 'Да'
    update = 'Исправить'
    cancel = 'Отмена'

class EmployeeSaveOrNotStateNewObjects(CallbackData, prefix='employee_save_or_not_new_objects'):
    action: EmployeeSaveOrNotNewObjectsAction

def build_employee_type_new_object_kb():
    print('KWYBOARD_NEWTYPW_EMPLOYEE_OBJETCS')
    print(EmployeeTypeNewObjects)
    flat = InlineKeyboardButton(
        text=EmployeeTypeNewObjectsAction.flat.value,
        callback_data=EmployeeTypeNewObjects(action=EmployeeTypeNewObjectsAction.flat).pack()
    )
    house = InlineKeyboardButton(
        text=EmployeeTypeNewObjectsAction.house.value,
        callback_data=EmployeeTypeNewObjects(action=EmployeeTypeNewObjectsAction.house).pack()
    )

    cancel = InlineKeyboardButton(
        text=EmployeeTypeNewObjectsAction.cancel.value,
        callback_data=EmployeeTypeNewObjects(action=EmployeeTypeNewObjectsAction.cancel).pack()

    )

    first_line = [flat, house]
    second_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup

def build_employee_category_new_object_kb():
    print('KWYBOARD_CAT_EMPLOYEE_OBJETCS')

    living = InlineKeyboardButton(
        text=EmployeeCategoryNewObjectsAction.living.value,
        callback_data=EmployeeCategoryNewObjects(action=EmployeeCategoryNewObjectsAction.living).pack()
    )
    prom = InlineKeyboardButton(
        text=EmployeeCategoryNewObjectsAction.prom.value,
        callback_data=EmployeeCategoryNewObjects(action=EmployeeCategoryNewObjectsAction.prom).pack()
    )

    cancel = InlineKeyboardButton(
        text=EmployeeCategoryNewObjectsAction.cancel.value,
        callback_data=EmployeeCategoryNewObjects(action=EmployeeCategoryNewObjectsAction.cancel).pack()

    )
    society = InlineKeyboardButton(
        text=EmployeeCategoryNewObjectsAction.society.value,
        callback_data=EmployeeCategoryNewObjects(action=EmployeeCategoryNewObjectsAction.society).pack()

    )


    first_line = [living, society]
    second_line = [prom]
    third_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line, third_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup

def build_employee_district_new_object_kb():
    print('KWYBOARD_NEWTYPW_EMPLOYEE_OBJETCS')

    gsv = InlineKeyboardButton(
        text=EmployeeDistrictNewObjectsAction.gsv.value,
        callback_data=EmployeeDistrictNewObjects(action=EmployeeDistrictNewObjectsAction.gsv).pack()
    )

    cancel = InlineKeyboardButton(
        text=EmployeeCategoryNewObjectsAction.cancel.value,
        callback_data=EmployeeDistrictNewObjects(action=EmployeeDistrictNewObjectsAction.cancel).pack()

    )

    first_line = [gsv]
    second_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup

def build_employee_building_type_new_object_kb():
    print('KWYBOARD_Building_EMPLOYEE_OBJETCS')

    brick = InlineKeyboardButton(
        text=EmployeeBuildingTypeNewObjectsAction.brick.value,
        callback_data=EmployeeBuildingTypeNewObjects(action=EmployeeBuildingTypeNewObjectsAction.brick).pack()
    )

    cancel = InlineKeyboardButton(
        text=EmployeeBuildingTypeNewObjectsAction.cancel.value,
        callback_data=EmployeeBuildingTypeNewObjects(action=EmployeeBuildingTypeNewObjectsAction.cancel).pack()

    )

    first_line = [brick]
    second_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup

def build_employee_repair_state_new_object_kb():
    print('KWYBOARD_repaire_state_EMPLOYEE_OBJETCS')

    euro = InlineKeyboardButton(
        text=EmployeeRepairStateNewObjectsAction.euro.value,
        callback_data=EmployeeRepiarStateNewObjects(action=EmployeeRepairStateNewObjectsAction.euro).pack()
    )

    cancel = InlineKeyboardButton(
        text=EmployeeRepairStateNewObjectsAction.cancel.value,
        callback_data=EmployeeRepiarStateNewObjects(action=EmployeeRepairStateNewObjectsAction.cancel).pack()

    )

    first_line = [euro]
    second_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup

def build_employee_save_or_not_new_object_kb():
    print('KWYBOARD_save_EMPLOYEE_OBJETCS')

    yes = InlineKeyboardButton(
        text=EmployeeSaveOrNotNewObjectsAction.yes.value,
        callback_data=EmployeeSaveOrNotStateNewObjects(action=EmployeeSaveOrNotNewObjectsAction.yes).pack()
    )
    update = InlineKeyboardButton(
        text=EmployeeSaveOrNotNewObjectsAction.no.value,
        callback_data=EmployeeSaveOrNotStateNewObjects(action=EmployeeSaveOrNotNewObjectsAction.no).pack()
    )

    cancel = InlineKeyboardButton(
        text=EmployeeTypeNewObjectsAction.cancel.value,
        callback_data=EmployeeTypeNewObjects(action=EmployeeTypeNewObjectsAction.cancel).pack()

    )

    first_line = [yes, update]
    second_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup