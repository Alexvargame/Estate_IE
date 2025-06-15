from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode


#from estate_agency.estate_bot.db import BotDBClass

from estate_bot.keyboards.kb_auth_reg import build_auth_reg_kb
from estate_bot.keyboards.employee_kb.main_employee_kb import build_employee_kb

from .states import OrderRegister



choice_menu_dict = {
    4: build_employee_kb(),
}
#BotDB = BotDBClass(Path(__file__).resolve().parent.parent.parent / 'db.sqlite3')

from estate_bot.base_name import BotDB

router = Router(name='start_FCM')

@router.message(Command('start', prefix="!/"))
async def handlers_start_reg_auth(message: types.Message, state: FSMContext):
    print(message.from_user.id)
    print('DB-reg_AUTJ', BotDB.file)
    if (not BotDB.user_exists(message.from_user.id)):
        print('FCM')
        await message.answer(
            text=f"Добро пожаловать,, {markdown.hbold(message.from_user.first_name)} Выберите действие в меню!",
            parse_mode=ParseMode.HTML,
            reply_markup=build_auth_reg_kb(),
        )
        await state.set_state(OrderRegister.waiting_for_password)
        # await state.update_data(name=message.text)
        # d = state.get_data()
        # print(d)
    else:
        print('Y')
        await state.set_state(OrderRegister.waiting_for_check_password)
        await message.answer("Введите пароль:", reply_markup=types.ReplyKeyboardRemove())

        # await state.update_data(password=message.text)
        # data = await state.get_data()
        # print('DATA', data)

# async def input_password(message: types.Message, state: FSMContext):
#
#     await state.update_data(name=message.text)
#     await state.set_state(OrderRegister.waiting_for_password.state)
#     # salt=os.urandom(32)
#     # key = hashlib.pbkdf2_hmac('sha256', message.text.encode('utf-8'), salt, 100000)
#     # await state.update_data(salt=salt)
#     # await state.update_data(password=key)
#     await state.update_data(password=message.text)
#     data = await state.get_data()
#     print('DATA', data)
#     BotDB.add_user(message.from_user.id, data['name'],data['salt'],data['password'])
#     await message.bot.send_message(message.from_user.id,
#                                    f"Добро пожаловать, {message.from_user.first_name}. Выберите действие в меню",
#                                    reply_markup=kb.menu)
#     await state.finish()

@router.message(OrderRegister.waiting_for_check_password)
async def check_password(message: types.Message, state: FSMContext):
    await state.update_data(name=BotDB.get_username_user(message.from_user.id))
    await state.set_state(OrderRegister.waiting_for_check_password.state)
    await state.update_data(password=message.text)
    data = await state.get_data()
    print(BotDB.get_user_id(message.from_user.id))
    print('DATA', data)
    print('types', BotDB.get_types())
    user_profile = BotDB.get_user_profile(BotDB.get_user_id(message.from_user.id))
    print(message.from_user.id, user_profile[14], user_profile[15])
    if user_profile[14] == message.from_user.id and user_profile[15] == message.text:
            #user_profile[10]==hashlib.pbkdf2_hmac('sha256', message.text.encode('utf-8'), user_profile[11], 100000):
        print(user_profile[13])
        await message.bot.send_message(message.from_user.id,
                                       f"Добро пожаловать, {message.from_user.first_name}. Выберите действие в меню",
                                       reply_markup=choice_menu_dict[user_profile[16]])
                                       #build_employee_kb())
    else:
        await message.bot.send_message(message.from_user.id, "Проверьте правильность пароля")
        return
    await state.clear()