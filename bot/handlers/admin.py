# bot/handlers/admin.py

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.config import config
from bot.database import Booking
from sqlalchemy import select, update
from bot.database import async_session

router = Router()

@router.message(F.text.lower() == "view pending payments")
async def view_pending_payments(message: Message):
    if str(message.from_user.id) != config.admin_id:
        return

    async with async_session() as session:
        result = await session.execute(select(Booking).where(Booking.status == "pending"))
        bookings = result.scalars().all()

        if not bookings:
            await message.answer("No pending payments.")
            return

        for booking in bookings:
            text = (
                f"🧾 Booking ID: {booking.id}\n"
                f"👤 Name: {booking.name}\n"
                f"📞 Phone: {booking.phone}\n"
                f"📅 Dates: {booking.check_in} to {booking.check_out}\n"
                f"💳 Payment Proof:\n"
            )
            await message.answer_photo(booking.payment_proof, caption=text)

@router.message(F.text.lower().startswith("approve "))
async def approve_booking(message: Message):
    if str(message.from_user.id) != config.admin_id:
        return

    booking_id = message.text.split(" ", 1)[-1]

    async with async_session() as session:
        result = await session.execute(select(Booking).where(Booking.id == booking_id))
        booking = result.scalar_one_or_none()

        if not booking:
            await message.answer("❌ Booking not found.")
            return

        stmt = update(Booking).where(Booking.id == booking_id).values(status="approved")
        await session.execute(stmt)
        await session.commit()

        await message.answer(f"✅ Booking ID {booking_id} approved.")
