from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.states import BookingStates
from bot.translations import get_text
from bot.keyboards.menu import cancel_kb

router = Router()

@router.message(F.text.lower() == "book a room")
async def ask_name(message: types.Message, state: FSMContext):
    lang = message.from_user.language_code or "en"
    await state.set_state(BookingStates.name)
    await message.answer(get_text("ask_name", lang), reply_markup=cancel_kb(lang))

@router.message(BookingStates.name)
async def ask_dates(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    lang = message.from_user.language_code or "en"
    await state.set_state(BookingStates.dates)
    await message.answer(get_text("ask_dates", lang))

@router.message(BookingStates.dates)
async def ask_guests(message: types.Message, state: FSMContext):
    await state.update_data(dates=message.text)
    lang = message.from_user.language_code or "en"
    await state.set_state(BookingStates.guests)
    await message.answer(get_text("ask_guests", lang))

@router.message(BookingStates.guests)
async def confirm_booking(message: types.Message, state: FSMContext):
    await state.update_data(guests=message.text)
    data = await state.get_data()
    lang = message.from_user.language_code or "en"

    summary = (
        f"<b>{get_text('booking_summary', lang)}</b>\n\n"
        f"👤 <b>{get_text('name', lang)}:</b> {data['name']}\n"
        f"📅 <b>{get_text('dates', lang)}:</b> {data['dates']}\n"
        f"👥 <b>{get_text('guests', lang)}:</b> {data['guests']}\n\n"
        f"{get_text('payment_instruction', lang)}"
    )
    await message.answer(summary)
    await state.clear()
