from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



def back_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Back", callback_data="back")
    return kb.as_markup()
