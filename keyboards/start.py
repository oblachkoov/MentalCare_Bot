from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



def start_kb(role: str):
    kb = ReplyKeyboardBuilder()
    if role == 'client':

        kb.button(text="🧠 Tests")
        kb.button(text="🆘 Help Me")
        kb.button(text="👩‍⚕️ Specialists")
        kb.button(text="📅 Appointments ")
        kb.button(text="📔 My notes")
        kb.adjust(2, 3)
        return kb.as_markup(resize_keyboard=True)

    elif role == 'admin':
        kb.button(text="📨 Requests")
        kb.button(text="👥 My clients")
        kb.button(text="📜 History")
        kb.button(text="📤 Send material")
        kb.adjust(2, 2)
        return kb.as_markup(resize_keyboard=True)
