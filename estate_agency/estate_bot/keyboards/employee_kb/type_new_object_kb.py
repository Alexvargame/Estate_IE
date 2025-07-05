from enum import Enum
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


from estate_agency.estate_agency_apps.property.services import (PropertyTypeService, PropertyCategoryService,
                                                                DistrictService, BuildingTypeService,
                                                                RepairStateService, PropertyService)
from estate_agency.estate_agency_apps.property.repository import (PropertyTypeRepository, PropertyCategoryRepository,
                                                                DistrictRepository, RepairStateRepository,
                                                                BuildingTypeRepository, PropertyRepository
                                                                )
from estate_bot.dictionaries import get_dictionary_object
def create_enum_from_data(enum_name, data):
    enum_members = {item.transcription: item.name for item in data}
    enum_members['cancel'] = 'Отмена'
    return Enum(enum_name, enum_members)

def create_enum_from_property(enum_name, data):
    enum_members = {item.name: item.name for item in data}
    enum_members.pop('id', None)
    enum_members.pop('is_active', None)
    enum_members.pop('created_at', None)
    enum_members.pop('updated_at', None)
    enum_members.pop('employee', None)
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


EmployeeCategoryNewObjectsAction = create_enum_from_data('EmployeeCategoryNewObjectsAction',
                                                         PropertyCategoryService(PropertyCategoryRepository()).list_objects())
class EmployeeCategoryNewObjects(CallbackData, prefix='employee_category_new_objects'):
    action: EmployeeCategoryNewObjectsAction

EmployeeDistrictNewObjectsAction = create_enum_from_data('EmployeeDistrictObjectsAction',
                                                         DistrictService(DistrictRepository()).list_objects())

class EmployeeDistrictNewObjects(CallbackData, prefix='employee_district_new_objects'):
    action: EmployeeDistrictNewObjectsAction

EmployeeBuildingTypeNewObjectsAction = create_enum_from_data('EmployeeBuildingTypeNewObjectsAction',
                                                             BuildingTypeService(BuildingTypeRepository()).list_objects())

class EmployeeBuildingTypeNewObjects(CallbackData, prefix='employee_building_type_new_objects'):
    action: EmployeeBuildingTypeNewObjectsAction

EmployeeRepairStateNewObjectsAction = create_enum_from_data('EmployeeRepairStateNewObjectsAction',
                                                            RepairStateService(RepairStateRepository()).list_objects())
class EmployeeRepiarStateNewObjects(CallbackData, prefix='employee_repair_state_new_objects'):
    action: EmployeeRepairStateNewObjectsAction

class EmployeeSaveOrNotNewObjectsAction(Enum):
    yes = 'Да'
    update = 'Исправить'
    cancel = 'Отмена'

class EmployeeSaveOrNotStateNewObjects(CallbackData, prefix='employee_save_or_not_new_objects'):
    action: EmployeeSaveOrNotNewObjectsAction

EmployeeUpdateObjectAction = create_enum_from_property('EmployeeUpdateObjectAction',
                                                       PropertyService(PropertyRepository()).get_fields())
class EmployeeUpdateObject(CallbackData, prefix='employee_update_object'):
    action: EmployeeUpdateObjectAction

def build_employee_type_new_object_kb():
    builder = InlineKeyboardBuilder()
    for key, value in EmployeeTypeNewObjectsAction._member_map_.items():
        button = builder.button(
            text=value.value,
            callback_data=EmployeeTypeNewObjects(action=value).pack()
        )

    # flat = InlineKeyboardButton(
    #     text=EmployeeTypeNewObjectsAction.flat.value,
    #     callback_data=EmployeeTypeNewObjects(action=EmployeeTypeNewObjectsAction.flat).pack()
    # )
    # house = InlineKeyboardButton(
    #     text=EmployeeTypeNewObjectsAction.house.value,
    #     callback_data=EmployeeTypeNewObjects(action=EmployeeTypeNewObjectsAction.house).pack()
    # )

    # cancel = InlineKeyboardButton(
    #     text=EmployeeTypeNewObjectsAction.cancel.value,
    #     callback_data=EmployeeTypeNewObjects(action=EmployeeTypeNewObjectsAction.cancel).pack()
    #
    # )
    # cancel = builder.button(
    #     text=EmployeeTypeNewObjectsAction.cancel.value,
    #     callback_data=EmployeeTypeNewObjects(action=EmployeeTypeNewObjectsAction.cancel).pack()
    #
    # )

    # first_line = list_button_menu#[flat, house]
    # second_line = [cancel]
    # markup = InlineKeyboardMarkup(
    #     inline_keyboard=[first_line, second_line],
    #     # resize_keyboard=True,
    #     # one_time_keyboard=True,
    #
    # )
    builder.adjust(3, 1)
    return builder.as_markup()

def build_employee_category_new_object_kb():
    builder = InlineKeyboardBuilder()
    for key, value in EmployeeCategoryNewObjectsAction._member_map_.items():
        button = builder.button(
            text=value.value,
            callback_data=EmployeeCategoryNewObjects(action=value).pack()
        )

    builder.adjust(3, 1)
    return builder.as_markup()

def build_employee_district_new_object_kb():
    builder = InlineKeyboardBuilder()
    for key, value in EmployeeDistrictNewObjectsAction._member_map_.items():
        button = builder.button(
            text=value.value,
            callback_data=EmployeeDistrictNewObjects(action=value).pack()
        )
    builder.adjust(3, 1)
    return builder.as_markup()

def build_employee_building_type_new_object_kb():
    builder = InlineKeyboardBuilder()
    for key, value in EmployeeBuildingTypeNewObjectsAction._member_map_.items():
        button = builder.button(
            text=value.value,
            callback_data=EmployeeBuildingTypeNewObjects(action=value).pack()
        )

    builder.adjust(3, 1)
    return builder.as_markup()

def build_employee_repair_state_new_object_kb():
    builder = InlineKeyboardBuilder()
    for key, value in EmployeeRepairStateNewObjectsAction._member_map_.items():
        button = builder.button(
            text=value.value,
            callback_data=EmployeeRepiarStateNewObjects(action=value).pack()
        )

    builder.adjust(3, 1)
    return builder.as_markup()

def build_employee_save_or_not_new_object_kb():
    print('KWYBOARD_save_EMPLOYEE_OBJETCS')

    yes = InlineKeyboardButton(
        text=EmployeeSaveOrNotNewObjectsAction.yes.value,
        callback_data=EmployeeSaveOrNotStateNewObjects(action=EmployeeSaveOrNotNewObjectsAction.yes).pack()
    )
    update = InlineKeyboardButton(
        text=EmployeeSaveOrNotNewObjectsAction.update.value,
        callback_data=EmployeeSaveOrNotStateNewObjects(action=EmployeeSaveOrNotNewObjectsAction.update).pack()
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

def build_update_new_object_kb():
    builder = InlineKeyboardBuilder()
    print(EmployeeUpdateObjectAction._member_map_.items())
    verbose_names = {item.name: item.verbose_name for item in PropertyService(PropertyRepository()).get_fields()}
    print('verb', verbose_names)
    for key, value in EmployeeUpdateObjectAction._member_map_.items():
        # cb_data = EmployeeUpdateObject(action=value.value).pack()
        # print(f"Button: {verbose_names[value.value]} -> callback_data: {cb_data}")
        # button = builder.button(
        #     text=verbose_names[value.value],
        #     callback_data=cb_data
        # )
        button = builder.button(
            text=verbose_names[value.value],
            callback_data=EmployeeUpdateObject(action=value.value).pack()
        )

    builder.adjust(4)
    return builder.as_markup()