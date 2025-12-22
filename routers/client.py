# from aiogram import  Router
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext
#
# from keyboards.client import start_kb, get_back
#
#
# router = Router()
#
#
# @router.message(CommandStart())
# async def start_handler(message: Message, state: FSMContext):
#     await state.clear()
#     await message.answer("Welcome to MentalCare+!💙\n", reply_markup=start_kb())
#






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


@router.message(F.text == "🧠 Tests")
async def tests_handler(message: Message, state: FSMContext):
    await state.set_state(ClientForm.test_client)
    await message.answer(
        "🧠 Take the tests:",
        reply_markup=test_kb()
    )

@router.callback_query(F.data == "client_stress")
async def test_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer("""Hi…
I’m Stress. You probably already know me. Sometimes I slip in unnoticed, sometimes I make my presence loudly felt. I make your heart race, your thoughts get tangled, and sometimes you feel at your limit.

I know, it’s unpleasant… But I’m not your enemy. I’m here to warn you that something needs your attention. I’m a signal that you need to pause, take a deep breath, and give yourself a little time.

You can listen to me, or you can ignore me — the choice is yours. When you take a break, care for yourself, talk to friends, or simply rest, I retreat. And you know what? The more you learn to understand me, the less I scare you.

Let’s make a deal: I’ll be your signal, not your prison. Listen to me, take care of yourself, and we can coexist without destroying your mood or your well-being.""", reply_markup=get_back())


@router.callback_query(F.data == "client_burnout")
async def test_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer("""🔥 Burnout check:\n"
        "Burnout is emotional exhaustion caused by prolonged stress.\n"
        "Signs to watch for:\n"
        "• Constant fatigue\n"
        "• Loss of interest in work or study\n"
        "• Feeling irritable or cynical\n\n"
        "💡 Tip: Take time to rest, enjoy small hobbies, and connect with loved ones.\n"
        "If symptoms persist, consider consulting a psychologist.""", reply_markup=get_back())


@router.callback_query(F.data == "client_anxiety")
async def test_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer("""Anxiety check:\n"
        "Anxiety is a feeling of worry or fear that can interfere with daily life.\n"
        "Common signs include:\n"
        "• Restlessness or feeling on edge\n"
        "• Rapid heartbeat or sweating\n"
        "• Trouble concentrating\n\n"
        "💡 Tip: Practice deep breathing, short breaks, and mindfulness exercises.\n"
        "If symptoms persist, consider talking to a psychologist.""", reply_markup=get_back())


@router.message(F.text == "🆘 Help Me")
async def help_me_handler(message: Message, state: FSMContext):
    await state.set_state(HelpMeForm.help_me)
    await message.answer(
        "🆘 How can we help you?",
        reply_markup=help_kb()
    )




@router.callback_query(F.data == "sleep_issues")
async def sleep_issues_handler(cb: CallbackQuery):
    await cb.message.answer("""💤 Sleep Issues

Having trouble falling asleep or waking up tired is very common,
especially when you are stressed or overthinking.

Here are some gentle tips that may help tonight:

• Turn off your phone 30 minutes before sleep  
• Take slow, deep breaths for 1–2 minutes  
• Try going to bed at the same time every day  
• Write down your thoughts to clear your mind  
• Drink warm tea or water (no caffeine)

Remember: one bad night does not mean something is wrong with you.
Your body knows how to rest 🤍""",
        reply_markup=get_back()
    )

@router.callback_query(F.data == "talk_psychologist")
async def talk_psychologist_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer("""Need professional help? You can talk to a psychologist:

• Share your feelings safely
• Get advice for stress, anxiety, or sleep issues
• Sessions are confidential

Press ⏪ Back to return.""", reply_markup=get_back())



@router.message(F.text == "👩‍⚕️ Specialists")
async def specialists_handler(message: Message, state: FSMContext):
    await state.set_state(SpecialistsForm.specialists)
    await message.answer(
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
            "You can talk to Aliya about stress, anxiety, or sleep issues.\n"
            "Feel free to share your feelings safely.\n"
            "You can also send documents or photos for discussion.\n\n"
            "Press ⏪ Back to return."
        ),
        reply_markup=get_back()
    )


@router.callback_query(F.data == "psychologist_alex")
async def psychologist_alex_handler(cb: CallbackQuery):
    await cb.answer()
    await cb.message.answer_photo(
        photo="https://img.freepik.com/premium-photo/portrait-of-happy-and-smiling-male-psychologist-portrait-sitting-on-arm-chair-in-psychiatrist-office-or-therapy-room-friendly-and-professional-mental-healthcare-counselor-and-therapist-unveiling_31965-255546.jpg",
        caption=("""👨‍💼 You can share your documents, images, or audio files with Psychologist Alex.\n"
        "📝 Please include a brief description so the psychologist can better understand your situation.\n"
        "Alex will review your materials and provide feedback or advice during the consultation"""),
        reply_markup=get_back()
    )



@router.message(F.text == "📅 Appointments")
async def appointments_handler(message: Message, state: FSMContext):
    await state.set_state(AppointmentsForm.appointments)
    await message.answer(
        "📅 Your appointments:",
        reply_markup=appointments_kb()
    )


@router.callback_query(F.data == "my_appointments")
async def my_appointments_handler(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.answer(
        "📅 Your appointment schedule:\n"
        "You don’t have any upcoming consultations yet.\n"
        "Use this section to:\n"
        "• Book a new session with a psychologist\n"
        "• Cancel or reschedule existing sessions\n"
        "• View reminders for upcoming consultations",
        reply_markup=get_back()
    )

@router.callback_query(F.data == "book_session")
async def book_session_handler(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.answer(
        "➕ Book a session:\n"
        "Choose a psychologist and select a convenient time for your consultation.\n"
        "You can cancel or reschedule later if needed.",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "cancel_appointment")
async def cancel_appointment_handler(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.answer(
        "❌ Cancel appointment:\n"
        "Here you can cancel any of your upcoming consultations.\n"
        "Select the appointment you want to cancel, and it will be removed from your schedule.",
        reply_markup=get_back()
    )


@router.message(F.text == "📔 My notes")
async def my_notes_handler(message: Message, state: FSMContext):
    await state.set_state(MyNoticeForm.my_notice)
    await message.answer(
        "📔 Personal diary.\nYou can write your notes here.",
        reply_markup=my_notes_kb()
    )



@router.callback_query(F.data == "add_note")
async def add_note_handler(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.answer(
        "📝 Add a new note:\n"
        "Write your thoughts, feelings, or any observations here.\n"
        "Your notes are private and will be saved in your personal diary.",
        reply_markup=get_back()
    )


@router.callback_query(F.data == "view_notes")
async def view_notes_handler(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.answer(
        "📄 Your notes:\n— No notes yet.\n"
        "Add some notes using the 'Add note' button.",
        reply_markup=get_back()
    )




@router.message(F.text == "⬅️ Back")
async def back_handler(message: Message):
    await start_handler(message)
