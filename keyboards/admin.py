from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



def role_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="User", callback_data="role_user")
    kb.button(text="Psychologist", callback_data="role_psychologist")
    kb.button(text="Admin", callback_data="role_admin")

    return kb.as_markup()

def get_back():
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Back", callback_data="admin_back")
    return kb.as_markup(resize_keyboard=True)