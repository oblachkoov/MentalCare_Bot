from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from state.client import HelpMeForm


def start_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="🧠 Tests")
    kb.button(text="🆘 Help Me")
    kb.button(text="👩‍⚕️ Specialists")
    kb.button(text="📅 Appointments ")
    kb.button(text="📔 My notes")
    kb.adjust(2, 3)
    return kb.as_markup(resize_keyboard=True)

def test_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text="🧠 stress", callback_data="client_stress")
    kb.button(text="😱 burnout", callback_data="client_burnout")
    kb.button(text="😩 anxiety", callback_data="client_anxiety")

    return kb.as_markup(resize_keyboard=True)




def help_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text="💤 Sleep Issues", callback_data="sleep_issues")
    kb.button(text="💬 Talk to Psychologist", callback_data="talk_psychologist")

    kb.adjust(1)

    return kb.as_markup()


def specialists_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Psychologist Aliya", callback_data="psychologist_aliya")
    kb.button(text="Psychologist Alex", callback_data="psychologist_alex")
    kb.adjust(1)
    return kb.as_markup()



def appointments_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="📌 My appointments", callback_data="my_appointments")
    kb.button(text="➕ Book a session", callback_data="book_session")
    kb.button(text="❌ Cancel appointment", callback_data="cancel_appointment")
    kb.adjust(2)
    return kb.as_markup()


def my_notes_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="📝 Add note", callback_data="add_note")
    kb.button(text="📄 View notes", callback_data="view_notes")
    kb.adjust(1)
    return kb.as_markup()


def get_back():
    kb = ReplyKeyboardBuilder()
    kb.button(text="⬅️ Back")
    return kb.as_markup(resize_keyboard=True)
