from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery

from pathlib import Path

# import re
# import os
# import hashlib
from datetime import datetime
#from estate_bot.db import BotDBClass
# import courierbot.kb

from decimal import Decimal

#BotDB=BotDBClass(Path(__file__).resolve().parent.parent.parent/'db.sqlite3')
from estate_agency.estate_bot.base_name import BotDB
class OrderReg(StatesGroup):
    waiting_for_username=State()
    waiting_for_password=State()



# Обратите внимание: есть второй аргумент
async def reg_start(clbck: CallbackQuery, state: FSMContext):
    print('reg start')
    await clbck.message.answer("Введите ник:")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await state.set_state(OrderReg.waiting_for_username.state)

async def reg_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)

    await state.set_state(OrderReg.waiting_for_password.state)
    await message.bot.send_message(message.chat.id, "Введите пароль:")

async def reg(message: types.Message, state: FSMContext):

    # salt = os.urandom(32)
    # key = hashlib.pbkdf2_hmac('sha256', message.text.encode('utf-8'), salt, 100000)
    # await state.update_data(salt=salt)
    # await state.update_data(password=key)
    await state.update_data(password=message.text)
    user_data = await state.get_data()
    BotDB.add_user(user_data['username'], user_data['password'], False, '', 'a@gmail.com', False, True, datetime.now(),'')
    BotDB.add_user_profile(user_data['username'],BotDB.check_user(user_data['username'],user_data['password']),'seller',message.chat.id,user_data['password'])#,user_data['salt'])
    await message.bot.send_message(message.from_user.id,
                                       f"Добро пожаловать, {message.from_user.first_name}. Выберите действие в меню",
                                       reply_markup=courierbot.kb.menu)

def register_handlers_reg(dp: Dispatcher):
    dp.register_callback_query_handler(reg_start, lambda callback_query: callback_query.data == "reg",state="*")
    #dp.register_message_handler(earned_start, commands="earned", state="*")
    dp.register_message_handler(reg_username, state=OrderReg.waiting_for_username)
    dp.register_message_handler(reg, state=OrderReg.waiting_for_password)
    #dp.register_message_handler(earned_sum_chosen, state=OrderEarned.waiting_for_earned_sum)
