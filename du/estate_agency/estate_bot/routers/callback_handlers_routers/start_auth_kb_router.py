from aiogram import F, Router, types
from aiogram.types import CallbackQuery
from estate_agency.estate_bot.keyboards.kb_auth_reg import RegDataAction, RegData


router = Router(name='reg_auth')



@router.callback_query(
    RegData.filter(F.action == RegDataAction.reg),
                       )
async def start_reg(callback_query: CallbackQuery):
    print("REG")
    await callback_query.message.answer(
        text=f"Введите ник:",
        reply_markup=types.ReplyKeyboardRemove()
    )

@router.callback_query(RegData.filter(F.action == RegDataAction.auth))
async def start_auth(callback_query: CallbackQuery):

    print("AUTH", callback_query.answer(text='auth'))
    await callback_query.answer(
        text="Введите пароль:",
        #reply_markup=types.ReplyKeyboardRemove()
    )


@router.callback_query(RegData.filter(F.action == RegDataAction.cancel))
async def start_cancel(callback_query: CallbackQuery):
    print("CANCEL")
    await callback_query.answer(
        text="Введите пароль:",
        #reply_markup=types.ReplyKeyboardRemove()
    )
    # await message.bot.send_message(message.from_user.id, f'Hi')
    #
    # if (not BotDB.user_exists(message.from_user.id)):
    #     print('N')
    #     #await message.answer("Введите логин сайта:", reply_markup=types.ReplyKeyboardRemove())
    #     await message.bot.send_message(message.from_user.id,
    #                                    f"Добро пожаловать, {message.from_user.first_name}. Выберите действие в меню",
    #                                    reply_markup=kb_auth_reg.menu)
    #     await state.set_state(OrderRegister.waiting_for_password)
    # else:
    #     print('Y')
    #     await message.answer("Введите пароль:", reply_markup=types.ReplyKeyboardRemove())
    #     await state.set_state(OrderRegister.waiting_for_check_password)