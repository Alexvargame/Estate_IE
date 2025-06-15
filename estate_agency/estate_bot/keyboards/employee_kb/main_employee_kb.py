
from enum import Enum
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,)
from aiogram.filters.callback_data import CallbackData


class EmployeeDataAction(Enum):
    reports = 'reports'
    objects = 'objects'
    cancel = 'cancel'
    clients = 'clients'
    search = 'search'

class EmployeeData(CallbackData, prefix='employee'):
    action: EmployeeDataAction



def build_employee_kb():
    print ('KWYBOARD_EMPLOYEE')

    objects= InlineKeyboardButton(
        text="📝Объекты",
        callback_data=EmployeeData(action=EmployeeDataAction.objects).pack()
    )
    clients = InlineKeyboardButton(
        text="🖼 Клиенты",
        callback_data=EmployeeData(action=EmployeeDataAction.clients).pack()
    )
    reports = InlineKeyboardButton(
        text='Отчеты',
        callback_data=EmployeeData(action=EmployeeDataAction.reports).pack()
    )
    search = InlineKeyboardButton(
        text='Поиск',
        callback_data=EmployeeData(action=EmployeeDataAction.search).pack()
    )
    cancel = InlineKeyboardButton(
        text='Отмена',
        callback_data=EmployeeData(action=EmployeeDataAction.cancel).pack()

    )

    first_line = [objects, clients]
    second_line = [reports, search]
    third_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line, third_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup


# menu = [
#     [InlineKeyboardButton(text="📝 Мои доставки", callback_data="delivery"),
#     InlineKeyboardButton(text="🖼 Добавить поступления", callback_data="auth_reg")],
#     [InlineKeyboardButton(text="💳 Отчеты", callback_data="reports"),
#     InlineKeyboardButton(text="💰 Поиск", callback_data="search")],
#     [InlineKeyboardButton(text="💎 Баланс пользователя", callback_data="balance"),
#     InlineKeyboardButton(text="🎁 Отмена", callback_data="cancel")],
# ]
# menu = InlineKeyboardMarkup(inline_keyboard=menu)
# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
#
# menu_delivery_info = [
#     [KeyboardButton("📝 Доставлено"),
#     KeyboardButton("🎁 Назад к списку")]
# ]
# menu_delivery_info = ReplyKeyboardMarkup(menu_delivery_info,resize_keyboard=True)
#
# menu_delivery_info_report = [
#     [KeyboardButton("Назад к списку"),
#     KeyboardButton("Отмена")]
# ]
# menu_delivery_info_report = ReplyKeyboardMarkup(menu_delivery_info_report,resize_keyboard=True)