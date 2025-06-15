from enum import Enum
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,)
from aiogram.filters.callback_data import CallbackData

#from estate_agency.estate_agency_apps.property.selectors import property_type_list
# file = Path(__file__).resolve().parent.parent/'selectors.py'

class EmployeeObjectsAction(Enum):
    # def __init__(self, data):
    #     for d in data:
    #         print(d.__name__)
    add_new = 'add_new'
    flats = 'flats'
    house = 'houses'
    cancel = 'cancel'
    all = 'all'
    search = 'search'


class EmployeeObjects(CallbackData, prefix='employee_objects'):
    action: EmployeeObjectsAction



def build_employee_type_objects_kb():
    print('KWYBOARD_EMPLOYEE_OBJETCS')
    #
    add_new = InlineKeyboardButton(
        text="📝Добавить новый объект",
        callback_data=EmployeeObjects(action=EmployeeObjectsAction.add_new).pack()
    )
    flats= InlineKeyboardButton(
        text="📝Квартиры",
        callback_data=EmployeeObjects(action=EmployeeObjectsAction.flats).pack()
    )
    houeses = InlineKeyboardButton(
        text="🖼 Дома",
        callback_data=EmployeeObjects(action=EmployeeObjectsAction.house).pack()
    )
    all = InlineKeyboardButton(
        text='Все',
        callback_data=EmployeeObjects(action=EmployeeObjectsAction.all).pack()
    )
    search = InlineKeyboardButton(
        text='Поиск',
        callback_data=EmployeeObjects(action=EmployeeObjectsAction.search).pack()
    )
    cancel = InlineKeyboardButton(
        text='Отмена',
        callback_data=EmployeeObjects(action=EmployeeObjectsAction.cancel).pack()

    )

    add_new = [add_new]
    first_line = [flats, houeses]
    second_line = [all]
    third_line = [search]
    forth_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[add_new, first_line, second_line, third_line, forth_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup
