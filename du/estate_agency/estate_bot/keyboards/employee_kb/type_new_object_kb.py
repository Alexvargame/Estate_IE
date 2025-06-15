from enum import Enum
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,)
from aiogram.filters.callback_data import CallbackData

#from estate_agency.estate_agency_apps.property.selectors import property_type_list
# file = Path(__file__).resolve().parent.parent/'selectors.py'

class EmployeeObjectsAction(Enum):
    # def __init__(self, data):
    #     for d in data:
    #         print(d.__name__)
    flats = 'flats'
    house = 'houses'
    cancel = 'cancel'
    all = 'all'


class EmployeeObjects(CallbackData, prefix='employee_objects'):
    action: EmployeeObjectsAction



def build_employee_type_objects_kb():
    print('KWYBOARD_EMPLOYEE_OBJETCS')
    #print('PTLIST', property_type_list())
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
    cancel = InlineKeyboardButton(
        text='Отмена',
        callback_data=EmployeeObjects(action=EmployeeObjectsAction.cancel).pack()

    )

    first_line = [flats, houeses]
    second_line = [all]
    third_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line, third_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup
