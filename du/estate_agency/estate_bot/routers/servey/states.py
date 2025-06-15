from aiogram.fsm.state import StatesGroup, State

class OrderRegister(StatesGroup):
    waiting_for_nickname = State()
    waiting_for_password = State()
    waiting_for_check_password = State()

class OrderEmployeeObjects(StatesGroup):
    waiting_for_type_object = State()
    waiting_for_id_object = State()

