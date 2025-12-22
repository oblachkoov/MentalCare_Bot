from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery


from keyboards.client import start_kb, get_back, test_kb, help_kb, specialists_kb, appointments_kb, my_notes_kb

from state.client import ClientForm, HelpMeForm, SpecialistsForm, AppointmentsForm, MyNoticeForm

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Welcome to MentalCare+! 💙\n Choose an action:",
        reply_markup=start_kb()
    )