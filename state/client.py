from aiogram.fsm.state import State, StatesGroup


class ClientForm(StatesGroup):
    test_client = State()


class HelpMeForm(StatesGroup):
    help_me = State()


class SpecialistsForm(StatesGroup):
    specialists = State()


class AppointmentsForm(StatesGroup):
    appointments = State()


class MyNoticeForm(StatesGroup):
    my_notice = State()