from aiogram.fsm.state import State, StatesGroup


class PsychologistForm(StatesGroup):
    psychologist = State()