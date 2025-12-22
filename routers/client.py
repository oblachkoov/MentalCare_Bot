from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import async_session

from keyboards.client import (
    test_kb, help_kb,
    specialists_kb, appointments_kb, my_notes_kb, get_back
)
from keyboards.start import start_kb as kb
from manager.notes import NoteManager
from model import User
from state.client import (
    ClientForm, HelpMeForm, SpecialistsForm,
    AppointmentsForm, MyNoticeForm
)

router = Router()


@router.callback_query(F.data == "user_tests")
async def menu(cb: CallbackQuery, user: User, state: FSMContext):
    await state.set_state(ClientForm.test_client)
    await cb.message.edit_text(
        "🧠 Take the tests:",
        reply_markup=test_kb()
    )


@router.callback_query(F.data == "client_stress")
async def test_stress_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text(
        "Hi…\n"
        "I’m Stress. You probably already know me.\n\n"
        "Sometimes I slip in unnoticed, sometimes I make my presence loudly felt.\n\n"
        "I’m not your enemy. I’m a signal that something needs your attention.\n\n"
        "Let’s make a deal: I’ll be your signal, not your prison 🤍",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "client_burnout")
async def test_burnout_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text(
        "🔥 Burnout check:\n\n"
        "Burnout is emotional exhaustion caused by prolonged stress.\n\n"
        "Signs:\n"
        "• Constant fatigue\n"
        "• Loss of interest\n"
        "• Irritability\n\n"
        "💡 Tip: Take time to rest and recover.",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "client_anxiety")
async def test_anxiety_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text(
        "😟 Anxiety check:\n\n"
        "Anxiety can interfere with daily life.\n\n"
        "Common signs:\n"
        "• Restlessness\n"
        "• Rapid heartbeat\n"
        "• Trouble concentrating\n\n"
        "💡 Tip: Try breathing exercises and rest.",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "user_help")
async def help_menu(cb: CallbackQuery, user: User, state: FSMContext):
    await state.set_state(HelpMeForm.help_me)
    await cb.message.edit_text(
        "🆘 How can we help you?",
        reply_markup=help_kb()
    )


@router.callback_query(F.data == "sleep_issues")
async def sleep_issues_handler(cb: CallbackQuery):
    await cb.message.edit_text(
        "💤 Sleep Issues\n\n"
        "Having trouble sleeping is common.\n\n"
        "Helpful tips:\n"
        "• No phone before bed\n"
        "• Deep breathing\n"
        "• Same bedtime daily\n"
        "• Write thoughts down\n\n"
        "Your body knows how to rest 🤍",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "talk_psychologist")
async def talk_psychologist_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text(
        "👩‍⚕️ Talk to a psychologist:\n\n"
        "• Safe space\n"
        "• Help with stress & anxiety\n"
        "• Confidential sessions",
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
async def psychologist_aliya_handler(cb: CallbackQuery):
    await cb.answer()
    await cb.message.answer_photo(
        photo="https://www.webminesllc.com/images/resource/3134716.jpg",
        caption=(
            "👩‍⚕️ Psychologist Aliya\n\n"
            "Specializes in stress, anxiety, and sleep issues."
        ),
        reply_markup=get_back()
    )


@router.callback_query(F.data == "psychologist_alex")
async def psychologist_alex_handler(cb: CallbackQuery):
    await cb.answer()
    await cb.message.answer_photo(
        photo="https://img.freepik.com/premium-photo/portrait-of-happy-and-smiling-male-psychologist-portrait-sitting-on-arm-chair-in-psychiatrist-office-or-therapy-room-friendly-and-professional-mental-healthcare-counselor-and-therapist-unveiling_31965-255546.jpg",
        caption=(
            "👨‍💼 Psychologist Alex\n\n"
            "You can send files with a short description."
        ),
        reply_markup=get_back()
    )


@router.callback_query(F.data == "my_appointments")
async def my_appointments_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text(
        "📅 You don’t have any upcoming appointments yet.",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "book_session")
async def book_session_handler(cb: CallbackQuery):
    await cb.message.edit_text(
        "➕ Book a session:\nChoose a psychologist and time.",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "cancel_appointment")
async def cancel_appointment_handler(cb: CallbackQuery):
    await cb.message.edit_text(
        "❌ Cancel appointment:\nSelect the appointment to cancel.",
        reply_markup=get_back()
    )


# Добавление заметки
@router.callback_query(F.data == "add_note")
async def add_note_handler(cb: CallbackQuery, user: User):
    await cb.message.edit_text("📝 Напишите ваш новый текст заметки (только текст, без файлов).",
                               reply_markup=get_back())
    # Устанавливаем состояние ожидания текста
    await MyNoticeForm.my_notice.set()


@router.message(MyNoticeForm.my_notice)
async def save_note_handler(message: Message, state: FSMContext, user: User):
    async with async_session() as session:
        manager = NoteManager(session)
        await manager.create_note(user_id=user.id, text=message.text)
    await message.answer("✅ Заметка сохранена!", reply_markup=my_notes_kb())
    await state.clear()


# Просмотр заметок
@router.callback_query(F.data == "view_notes")
async def view_notes_handler(cb: CallbackQuery, user: User):
    async with async_session() as session:
        manager = NoteManager(session)
        notes = await manager.get_user_notes(user.id)

    if not notes:
        await cb.message.edit_text("📄 Заметок пока нет.", reply_markup=get_back())
        return

    text = "📄 Ваши заметки:\n\n"
    for i, note in enumerate(notes, start=1):
        text += f"{i}. {note.text}\n"
        if note.file_url:
            text += f"📎 {note.file_url}\n"
        text += f"🕒 {note.created_at.strftime('%Y-%m-%d %H:%M')}\n\n"

    await cb.message.edit_text(text, reply_markup=get_back())


@router.callback_query(F.data == "view_notes")
async def view_notes_handler(cb: CallbackQuery):
    await cb.message.edit_text(
        "📄 No notes yet.",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "user_back")
async def back_to_menu(cb: CallbackQuery, user: User, state: FSMContext):
    await state.clear()
    await cb.message.edit_text(
        f"Welcome to MentalCare+ {user.full_name} ({user.role}) 💙\nChoose an action:",
        reply_markup=kb(user.role)
    )
