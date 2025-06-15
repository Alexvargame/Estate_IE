
from enum import Enum
from aiogram.types import( InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.filters.callback_data import CallbackData


class RegDataAction(Enum):
    reg = 'reg',
    auth = 'aurh'

class RegData(CallbackData, prefix='reg'):
    action: RegDataAction


def build_auth_reg_kb():
    reg_btn = InlineKeyboardButton(
        text = "📝Нет регистрации на сайте",
        callback_data=registrartion
    )
    auth_btn = InlineKeyboardButton(
        text="🖼 Есть регистрация на сайте",
        callback_data=auth,
    )
# menu = [
#     [InlineKeyboardButton(text="📝Нет регистрации на сайте", callback_data=reg_data),
#     InlineKeyboardButton(text="🖼 Есть регистрация на сайте", callback_data=auth_data)],
#     [InlineKeyboardButton(text="🎁 Отмена", callback_data="cancel")],
#
# ]
# menu = InlineKeyboardMarkup(
#     inline_keyboard=menu)
# exit_kb = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]],
#     resize_keyboard=True,
#    # one_time_keyboard=True,
# )
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])