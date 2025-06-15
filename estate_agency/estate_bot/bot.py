import asyncio
import logging
# import os
# import sys
# import django
import config

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
#from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher.filters import Text, IDFilter
# from aiogram.types import CallbackQuery

#from aiogram.enums.parse_mode import ParseMode

from routers import router as main_router


#from db import BotDBClass
# import kb


#from app.config_reader import load_config
# from handlers.auth import register_handlers_auth
# from handlers.reg import register_handlers_reg
# from handlers.delivery import register_handlers_delivery
# from handlers.reports import register_handlers_reports
# #from handlers.search import register_handlers_search
# from handlers.balance import register_handlers_balance

#from app.handlers.common import register_handlers_common
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# # Устанавливаем переменную окружения для настроек Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate_agency.config.django.base')
#
# # Инициализируем Django
# django.setup()
logger = logging.getLogger(__name__)


#BotDB = BotDBClass(Path(__file__).resolve().parent.parent/'estate_agency/estate_agency_apps/db_base.sqlite3')


class OrderRegister(StatesGroup):
    waiting_for_nickname = State()
    waiting_for_password = State()
    waiting_for_check_password = State()

#dp = Dispatcher(storage=MemoryStorage())
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать работу"),
        BotCommand(command="/cancel", description="Отмена"),
    ]
    await bot.set_my_commands(commands)
#
# @main_router.message(CommandStart())
# async def start(message, state: FSMContext):
#     await message.bot.send_message(message.from_user.id, f'Hi')
#
#     if (not BotDB.user_exists(message.from_user.id)):
#         print('N')
#         #await message.answer("Введите логин сайта:", reply_markup=types.ReplyKeyboardRemove())
#         await message.bot.send_message(message.from_user.id,
#                                        f"Добро пожаловать, {message.from_user.first_name}. Выберите действие в меню",
#                                        reply_markup=kb_auth_reg.menu)
#         await state.set_state(OrderRegister.waiting_for_password)
#     else:
#         print('Y')
#         await message.answer("Введите пароль:", reply_markup=types.ReplyKeyboardRemove())
#         await state.set_state(OrderRegister.waiting_for_check_password)

# async def input_password(message: types.Message, state: FSMContext):
#
#     await state.update_data(name=message.text)
#     await state.set_state(OrderRegister.waiting_for_password.state)
#     # salt=os.urandom(32)
#     # key = hashlib.pbkdf2_hmac('sha256', message.text.encode('utf-8'), salt, 100000)
#     # await state.update_data(salt=salt)
#     # await state.update_data(password=key)
#     await state.update_data(password=message.text)
#     data=await state.get_data()
#     BotDB.add_user(message.from_user.id, data['name'],data['salt'],data['password'])
#     await message.bot.send_message(message.from_user.id,
#                                    f"Добро пожаловать, {message.from_user.first_name}. Выберите действие в меню",
#                                    reply_markup=kb.menu)
#     await state.finish()
# async def check_password(message: types.Message, state: FSMContext):
#     await state.update_data(name=BotDB.get_name_user(message.from_user.id))
#     await state.set_state(OrderRegister.waiting_for_check_password.state)
#     await state.update_data(password=message.text)
#     data=await state.get_data()
#     print(BotDB.get_user_id(message.from_user.id))
#     user_profile=BotDB.get_user_profile(BotDB.get_user_id(message.from_user.id))
#     if user_profile[9]==message.from_user.id and user_profile[10]==message.text:
#             #user_profile[10]==hashlib.pbkdf2_hmac('sha256', message.text.encode('utf-8'), user_profile[11], 100000):
#         await message.bot.send_message(message.from_user.id,
#                                        f"Добро пожаловать, {message.from_user.first_name}. Выберите действие в меню",
#                                        reply_markup=kb.menu)
#     else:
#         await message.bot.send_message(message.from_user.id, "Проверьте правильность пароля")
#         return
#     await state.finish()
# async def cmd_cancel(message: types.Message, state: FSMContext):
#     await state.finish()
#     await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())
#     await message.bot.send_message(message.from_user.id,
#                                    "Выберите действие в меню",
#                                    reply_markup=kb.menu)


async def main():

    # Настройка логирования в stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    # Парсинг файла конфигурации
    #config = load_config("config/bot.ini")

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=config.BOT_TOKEN)#, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(main_router)
    # Регистрация хэндлеров
   #  #register_handlers_common(dp, config.tg_bot.admin_id)
   # dp.message.register(start)
   #  dp.register_message_handler(input_password, state=OrderRegister.waiting_for_password)
   #  dp.register_message_handler(check_password, state=OrderRegister.waiting_for_check_password)
   #  dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
   #  #dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
   # # dp.register_callback_query_handler(cmd_cancel, lambda callback_query: callback_query.data == "cancel", state="*")
   # # dp.register_callback_query_handler(cmd_cancel, lambda callback_query: callback_query.data == "cancel", state="*")
   #  register_handlers_delivery(dp)
   #  register_handlers_auth(dp)
   #  register_handlers_reg(dp)
   #  register_handlers_reports(dp)
   # # register_handlers_search(dp)
   #  register_handlers_balance(dp)

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
