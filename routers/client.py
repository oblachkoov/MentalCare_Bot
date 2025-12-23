from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.client import (
    test_kb,
    help_kb,
    specialists_kb,
    my_notes_kb,
    get_back, appointments_kb
)
from keyboards.start import start_kb
from manager.appointments import AppointmentManager
from manager.notes import NoteManager
from model import User
from state.client import (
    ClientForm,
    HelpMeForm,
    SpecialistsForm,
    MyNoticeForm
)
from config import async_sessionmaker, async_session

router = Router()



@router.callback_query(F.data == "user_tests")
async def tests_menu(cb: CallbackQuery, state: FSMContext):
    await state.set_state(ClientForm.test_client)
    await cb.message.edit_text(
        "🧠 Take the tests:",
        reply_markup=test_kb()
    )


@router.callback_query(F.data == "client_stress")
async def test_stress(cb: CallbackQuery):
    await cb.message.edit_text(
        "🧠 Stress\n\n"
        "I’m not your enemy.\n"
        "I’m a signal that something needs attention 🤍",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "client_burnout")
async def test_burnout(cb: CallbackQuery):
    await cb.message.edit_text(
        "🔥 Burnout\n\n"
        "Signs:\n"
        "• Constant fatigue\n"
        "• Loss of interest\n"
        "• Irritability\n\n"
        "💡 Take time to rest.",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "client_anxiety")
async def test_anxiety(cb: CallbackQuery):
    await cb.message.edit_text(
        "😟 Anxiety\n\n"
        "Signs:\n"
        "• Restlessness\n"
        "• Rapid heartbeat\n"
        "• Trouble focusing\n\n"
        "💡 Try breathing exercises.",
        reply_markup=get_back()
    )



@router.callback_query(F.data == "user_help")
async def help_menu(cb: CallbackQuery, state: FSMContext):
    await state.set_state(HelpMeForm.help_me)
    await cb.message.edit_text(
        "🆘 How can we help you?",
        reply_markup=help_kb()
    )


@router.callback_query(F.data == "sleep_issues")
async def sleep_issues(cb: CallbackQuery):
    await cb.message.edit_text(
        "💤 Sleep issues\n\n"
        "Tips:\n"
        "• No phone before bed\n"
        "• Same bedtime\n"
        "• Write thoughts down",
        reply_markup=get_back()
    )



@router.callback_query(F.data == "user_specialists")
async def specialists_menu(cb: CallbackQuery, state: FSMContext):
    await state.set_state(SpecialistsForm.specialists)
    await cb.message.edit_text(
        "👩‍⚕️ Available specialists:",
        reply_markup=specialists_kb()
    )


@router.callback_query(F.data == "psychologist_aliya")
async def psychologist_aliya(cb: CallbackQuery):
    await cb.message.answer_photo(
        photo="https://www.webminesllc.com/images/resource/3134716.jpg",
        caption="👩‍⚕️ Psychologist Aliya\n\nStress & anxiety specialist",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "psychologist_alex")
async def psychologist_alex(cb: CallbackQuery):
    await cb.message.answer_photo(
        photo="https://img.freepik.com/premium-photo/portrait-of-happy-and-smiling-male-psychologist-portrait-sitting-on-arm-chair-in-psychiatrist-office-or-therapy-room-friendly-and-professional-mental-healthcare-counselor-and-therapist-unveiling_31965-255546.jpg",
        caption="👨‍⚕️ Psychologist Alex\n\nYou can send files with a description.",
        reply_markup=get_back()
    )




@router.callback_query(F.data == "user_appointments")
async def user_appointments(cb: CallbackQuery):
    await cb.message.edit_text(
        "📅 Appointments menu:",
        reply_markup=appointments_kb()
    )





@router.callback_query(F.data == "my_appointments")
async def my_appointments(cb: CallbackQuery, user: User):
    async with async_session() as session:
        manager = AppointmentManager(session)
        appointments = await manager.get_client_appointments(user.id)

    if not appointments:
        await cb.message.edit_text("📅 You have no appointments yet.", reply_markup=get_back())
        return

    text = "📅 Your appointments:\n\n"
    for i, appt in enumerate(appointments, 1):
        status = appt.status
        time = appt.time.strftime("%Y-%m-%d %H:%M") if appt.time else "Not set"
        psychologist = f"ID {appt.psychologist_id}" if appt.psychologist_id else "Not assigned"
        text += f"{i}. 🕒 {time} | 👩‍⚕️ {psychologist} | Status: {status}\n"

    await cb.message.edit_text(text, reply_markup=get_back())



@router.callback_query(F.data == "book_session")
async def book_session(cb: CallbackQuery, user: User):
    async with async_session() as session:
        manager = AppointmentManager(session)
        appointment = await manager.create(client_id=user.id)

    await cb.message.edit_text(
        f"✅ Appointment request created! (ID {appointment.id})\n"
        "Waiting for psychologist confirmation.",
        reply_markup=get_back()
    )




@router.callback_query(F.data == "user_notes")
async def notes_menu(cb: CallbackQuery):
    await cb.message.edit_text(
        "📔 My notes:",
        reply_markup=my_notes_kb()
    )


@router.callback_query(F.data == "add_note")
async def add_note(cb: CallbackQuery, state: FSMContext):
    await state.set_state(MyNoticeForm.my_notice)
    await cb.message.edit_text(
        "📝 Send note text:",
        reply_markup=get_back()
    )


@router.message(MyNoticeForm.my_notice)
async def save_note(message: Message, state: FSMContext, user: User):
    async with async_session() as session:
        manager = NoteManager(session)
        await manager.create(
            user_id=user.id,
            text=message.text
        )

    await state.clear()
    await message.answer(
        "✅ Note saved!",
        reply_markup=my_notes_kb()
    )


@router.callback_query(F.data == "view_notes")
async def view_notes(cb: CallbackQuery, user: User):
    async with async_session() as session:
        manager = NoteManager(session)
        notes = await manager.get_user_notes(user.id)

    if not notes:
        await cb.message.edit_text(
            "📄 No notes yet.",
            reply_markup=get_back()
        )
        return

    text = "📄 Your notes:\n\n"
    for i, note in enumerate(notes, 1):
        text += (
            f"{i}. {note.text}\n"
            f"🕒 {note.created_at:%Y-%m-%d %H:%M}\n\n"
        )

    await cb.message.edit_text(text, reply_markup=get_back())



@router.callback_query(F.data == "user_back")
async def back_to_menu(cb: CallbackQuery, state: FSMContext, user: User):
    await state.clear()
    await cb.message.answer(
        f"Welcome to MentalCare+ {user.full_name} 💙",
        reply_markup=start_kb(user.role)
    )
