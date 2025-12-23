from aiogram.fsm.state import State, StatesGroup

class AdminForm(StatesGroup):
    admin_set_role = State()
