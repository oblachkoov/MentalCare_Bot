from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from config import async_session
from keyboards.psychologist import back_kb
from keyboards.start import start_kb
from manager.appointments import AppointmentManager
from model import User
from state.psychologist import PsychologistForm

router = Router()



@router.callback_query(F.data == "psy_requests")
async def psy_requests_handler(cb: CallbackQuery, state: FSMContext):
    await state.set_state(PsychologistForm.psychologist)

    async with async_session() as session:
        manager = AppointmentManager(session)
        requests = await manager.get_new_requests()

    if not requests:
        text = "📨 No new appointment requests."
    else:
        text = "📨 New appointment requests:\n\n"
        for ap in requests:
            text += (
                f"🆔 ID: {ap.id}\n"
                f"👤 Client: {ap.client_id}\n"
                f"👉 Take: take_{ap.id}\n\n"
            )

    await cb.message.edit_text(text, reply_markup=back_kb())
    await cb.answer()




@router.message(F.text.isdigit(), PsychologistForm.psychologist)
async def take_client_handler(message: Message,user:User, state: FSMContext):
    appointment_id = int(message.text)

    async with async_session() as session:
        manager = AppointmentManager(session)
        await manager.take_client(
            appointment_id=appointment_id,
            psychologist_id=user.id
        )

    await message.answer(
        "✅ Client successfully taken.",
        reply_markup=back_kb()
    )

    await state.clear()



@router.callback_query(F.data == "psy_my_clients")
async def psy_my_clients_handler(cb: CallbackQuery, state: FSMContext):
    await state.set_state(PsychologistForm.psychologist)

    async with async_session() as session:
        manager = AppointmentManager(session)
        clients = await manager.get_my_clients(cb.from_user.id)

    if not clients:
        text = "👥 You have no active clients."
    else:
        text = "👥 My clients:\n\n"
        for ap in clients:
            text += (
                f"🆔 ID: {ap.id}\n"
                f"👤 Client: {ap.client_id}\n"
                f"✔️ Reply with the ID to mark as done\n\n"
            )

    await cb.message.edit_text(text, reply_markup=back_kb())
    await cb.answer()




@router.message(F.text.isdigit(), PsychologistForm.psychologist)
async def done_client_handler(message: Message, user: User, state: FSMContext):
    appointment_id = int(message.text)

    async with async_session() as session:
        manager = AppointmentManager(session)
        await manager.mark_done(
            appointment_id=appointment_id,
            psychologist_id=user.id
        )

    await message.answer(
        "✔️ Client marked as done.",
        reply_markup=back_kb()
    )

    await state.clear()




@router.callback_query(F.data == "psy_history")
async def psy_history_handler(cb: CallbackQuery):
    async with async_session() as session:
        manager = AppointmentManager(session)
        history = await manager.get_history_appointments(cb.from_user.id)

    if not history:
        text = "📜 History is empty."
    else:
        text = "📜 Appointment history:\n\n"
        for ap in history:
            text += (
                f"🆔 ID: {ap.id}\n"
                f"👤 Client: {ap.client_id}\n"
                f"⏰ Finished: {ap.finished_at}\n\n"
            )

    await cb.message.edit_text(text, reply_markup=back_kb())
    await cb.answer()




@router.callback_query(F.data == "psy_send_material")
async def psy_send_material_handler(cb: CallbackQuery):
    await cb.message.edit_text(
        "📤 Upload PDF, image, or audio for the client please!",
        reply_markup=back_kb()
    )
    await cb.answer()



@router.callback_query(F.data == "back")
async def back_handler(cb: CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await cb.message.edit_text(
        f"Welcome to MentalCare+ {user.full_name} ({user.role}) 💙\nChoose an action:",
        reply_markup=start_kb(user.role)
    )
    await cb.answer()
