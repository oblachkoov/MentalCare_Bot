from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.psychologist import psychologist_kb, get_back
from state.psychologist import PsychologistForm

router = Router()

@router.message(CommandStart())
async def psychologist_handler(message: Message):
    await message.answer(
         "Welcome, Psychologist! ❤️\nChoose an action:",

    )


@router.message(F.text == "📨 Requests")
async def requests_handler(message: Message):
    await message.answer(
        "📨 Here are the new appointment requests.",
        reply_markup=get_back()
    )


@router.message(F.text == "📨 Requests")
async def requests_handler(message: Message, state: FSMContext):
    await state.set_state(PsychologistForm.psychologist)
    await message.answer(
        "📨 Here are the new appointment requests.\n"
        "You can confirm, reschedule, or cancel them.",
        reply_markup=psychologist_kb()
    )


@router.message(F.text == "👥 My clients")
async def my_clients_handler(message: Message):
    await message.answer(
        "👥 Your clients:\n- Client1\n- Client2",
        reply_markup=get_back()
    )


@router.message(F.text == "📤 Send material")
async def send_material_handler(message: Message):
    await message.answer(
        "📤 Upload PDF, image, or audio for the client please!",
        reply_markup=get_back()
    )

@router.message(F.text == "⬅️ Back")
async def back_handler(message: Message):
    await psychologist_handler(message)