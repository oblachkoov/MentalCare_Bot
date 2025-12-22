from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def psychologist_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="📨 Requests")
    kb.button(text="👥 My clients")
    kb.button(text="📜 History")
    kb.button(text="📤 Send material")
    kb.adjust(2, 2)
    return kb.as_markup(resize_keyboard=True)

def get_back():
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Back")
    return kb.as_markup(resize_keyboard=True)
