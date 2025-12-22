from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_kb(role: str):
    kb = InlineKeyboardBuilder()

    # 👤 USER
    if role == 'user':
        kb.button(text="🧠 Tests", callback_data="user_tests")
        kb.button(text="🆘 Help Me", callback_data="user_help")
        kb.button(text="👩‍⚕️ Specialists", callback_data="user_specialists")
        kb.button(text="📅 Appointments", callback_data="user_appointments")
        kb.button(text="📔 My notes", callback_data="user_notes")
        kb.adjust(2, 3)

    # 👩‍⚕️ PSYCHOLOGIST
    elif role == 'psychologist':
        kb.button(text="📨 Requests", callback_data="psy_requests")
        kb.button(text="👥 My clients", callback_data="psy_my_clients")
        kb.button(text="📜 History", callback_data="psy_history")
        kb.button(text="📤 Send material", callback_data="psy_send_material")
        kb.adjust(2, 2)

    # 🛡 ADMIN
    elif role == 'admin':
        kb.button(text="👥 Users", callback_data="admin_users")
        kb.button(text="✅ Verify", callback_data="admin_verify")
        kb.button(text="🎭 Set role", callback_data="admin_set_role")
        kb.button(text="🚫 Block", callback_data="admin_block")
        kb.button(text="📜 Logs", callback_data="admin_logs")
        kb.adjust(2, 3)

    return kb.as_markup()
