from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from config import async_session
from keyboards.admin import role_kb, get_back
from manager.user import UserManager
from keyboards.start import start_kb
from model import User
from aiogram.fsm.context import FSMContext
from state.admin import AdminForm

router = Router()




@router.callback_query(F.data == "admin_users")
async def admin_users_handler(cb: CallbackQuery):
    async with async_session() as session:
        manager = UserManager(session)
        users = await manager.list()

    if not users:
        text = "👥 No users found."
    else:
        text = "👥 Users list:\n\n"
        for u in users:
            text += f"🆔 {u.id} | {u.full_name} | Role: {u.role or 'None'}\n"

    await cb.message.edit_text(text)
    await cb.answer()




@router.callback_query(F.data == "admin_verify")
async def admin_verify_handler(cb: CallbackQuery):
    async with async_session() as session:
        manager = UserManager(session)
        users = await manager.list()

    unverified = [u for u in users if not u.role]
    if not unverified:
        text = "✅ All users are verified."
    else:
        text = "✅ Users to verify:\n\n"
        for u in unverified:
            text += f"🆔 {u.id} | {u.full_name}\n"

    await cb.message.edit_text(text)
    await cb.answer()




@router.callback_query(F.data == "admin_set_role")
async def admin_set_role_handler(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text(
        "🎭 Send the user ID to set role.\nExample: `123456789`"
    )
    await state.set_state(AdminForm.admin_set_role)
    await cb.answer()



@router.message(F.text, AdminForm.admin_set_role)
async def choose_role_handler(message: Message, state: FSMContext):
    try:
        user_id = int(message.text)
    except ValueError:
        await message.answer("❌ Invalid user ID. Send a number.")
        return

    await state.update_data(user_id=user_id)
    await message.answer("Select role for this user:", reply_markup=role_kb())



@router.callback_query(F.data.startswith("role_"))
async def set_role_callback(cb: CallbackQuery, state: FSMContext):
    role = cb.data.split("_")[1]
    data = await state.get_data()
    user_id = data.get("user_id")
    if not user_id:
        await cb.answer("❌ User ID not found. Start again.", show_alert=True)
        return

    async with async_session() as session:
        manager = UserManager(session)
        user = await manager.update_role(user_id, role)

    await cb.message.edit_text(f"✅ Role of {user.full_name} set to {user.role}.", reply_markup=get_back())
    await state.clear()
    await cb.answer()



@router.callback_query(F.data == "admin_logs")
async def admin_logs_handler(cb: CallbackQuery):
    text = "📜 Logs functionality not implemented yet."
    await cb.message.edit_text(text,reply_markup=get_back())
    await cb.answer()



@router.callback_query(F.data == "admin_back")
async def back_handler(cb: CallbackQuery, user: User):
    await cb.message.edit_text(
        f"Welcome {user.full_name} ({user.role})!\nChoose an action:",
        reply_markup=start_kb(user.role)
    )
    await cb.answer()
