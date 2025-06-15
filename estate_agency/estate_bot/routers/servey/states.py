from aiogram.fsm.state import StatesGroup, State

class OrderRegister(StatesGroup):
    waiting_for_nickname = State()
    waiting_for_password = State()
    waiting_for_check_password = State()

class OrderEmployeeObjects(StatesGroup):
    waiting_for_type_object = State()
    waiting_for_id_object = State()


class OrderNewObject(StatesGroup):
    waiting_for_type_object = State()
    waiting_for_category_object = State()
    waiting_for_district_object = State()
    waiting_for_address_object = State()
    waiting_for_rooms_count_object = State()
    waiting_for_total_area_object = State()
    waiting_for_living_area_object = State()
    waiting_for_floor_object = State()
    waiting_for_total_floor_object = State()
    waiting_for_building_type_object = State()
    waiting_for_repair_state_object = State()
    waiting_for_infrastructure_object = State()
    waiting_for_check_object = State()
    waiting_for_save_or_no_object = State()
