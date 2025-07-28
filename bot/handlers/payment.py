from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.config import load_config
from bot.translations import get_text
from bot.keyboards.menu import confirm_cancel_kb

router = Router()
config = load_config()

PAYMENT_DETAILS = f"""
🏦 <b>Bank Transfer / UPI</b>

🏛️ <b>Bank:</b> {config.bank_name}
🔢 <b>A/C No.:</b> {config.account_number}
🏷️ <b>IFSC:</b> {config.ifsc_code}
💸 <b>UPI:</b> {config.upi_id}
📞 <b>Hotel:</b> {config.hotel_contact}

{get_text("send_payment_proof", "en")}
"""

@router.message(F.text.lower() == "proceed to payment")
async def send_payment_details(message: types.Message, state: FSMContext):
    lang = message.from_user.language_code or "en"
    await message.answer(PAYMENT_DETAILS, reply_markup=confirm_cancel_kb(lang))

@router.message(F.photo)
async def handle_payment_proof(message: types.Message):
    lang = message.from_user.language_code or "en"
    admin_id = config.admin_id
    caption = f"🧾 <b>New Payment Proof</b>\nFrom: @{message.from_user.username or message.from_user.id}"

    await message.forward(chat_id=admin_id)
    await message.bot.send_message(admin_id, caption)
    await message.answer(get_text("payment_received", lang))
