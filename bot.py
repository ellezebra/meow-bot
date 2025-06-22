
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils import logging
from dotenv import load_dotenv

import asyncio

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TO_ID = os.getenv("TO_ID")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Кнопки
start_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🎈 Хочу оформление")]],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        """Привет! Я бот студии Meow Balloons 🎉
Нажми кнопку ниже, чтобы оставить заявку.""",
        reply_markup=start_kb
    )

@dp.message(lambda m: m.text == "🎈 Хочу оформление")
async def handle_request(message: types.Message):
    user = message.from_user
    text = f"""🎉 Новая заявка от @{user.username or user.id}
Имя: {user.full_name}"""
    await bot.send_message(chat_id=TO_ID, text=text)
    await message.answer("Спасибо за заявку! Мы скоро с вами свяжемся.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
