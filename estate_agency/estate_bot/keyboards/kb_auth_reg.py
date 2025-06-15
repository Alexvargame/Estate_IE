
from enum import Enum
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,)
from aiogram.filters.callback_data import CallbackData


class RegDataAction(Enum):
    reg = 'reg'
    auth = 'auth'
    cancel = 'cancel'
    link = 'link'

class RegData(CallbackData, prefix='reg'):
    action: RegDataAction


def build_auth_reg_kb():
    print ('KWYBOARD')
    reg_btn = InlineKeyboardButton(
        text="📝Нет регистрации на сайте",
        callback_data=RegData(action=RegDataAction.reg).pack()
    )
    auth_btn = InlineKeyboardButton(
        text="🖼 Есть регистрация на сайте",
        callback_data=RegData(action=RegDataAction.auth).pack()
    )
    cancel = InlineKeyboardButton(
        text='Cancel',
        callback_data=RegData(action=RegDataAction.cancel).pack()

    )

    first_line = [reg_btn, auth_btn]
    second_line = [cancel]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[first_line, second_line],
        # resize_keyboard=True,
        # one_time_keyboard=True,

    )
    return markup
