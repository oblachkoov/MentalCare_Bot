from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery


from keyboards.start import start_kb
from model import User

from state.client import ClientForm, HelpMeForm, SpecialistsForm, AppointmentsForm, MyNoticeForm

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, user: User):
    await message.answer(
        f"Welcome to MentalCare+ {user.full_name} {user.role} ! 💙\n Choose an action:",
        reply_markup=start_kb(user.role)
    )