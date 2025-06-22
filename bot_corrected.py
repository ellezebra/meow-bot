
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TO_ID = os.getenv("TO_ID")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Кнопки
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton("🎈 Хочу оформление"))

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("Привет! Я бот студии Meow Balloons 🎉\nНажми кнопку ниже, чтобы оставить заявку.", reply_markup=start_kb)

@dp.message_handler(lambda message: message.text == "🎈 Хочу оформление")
async def handle_request(msg: types.Message):
    text = f"🎉 Новая заявка от @{msg.from_user.username or msg.from_user.id}\nИмя: {msg.from_user.full_name}"
    await bot.send_message(chat_id=TO_ID, text=text)
    await msg.answer("Спасибо за заявку! Мы скоро с вами свяжемся.")

if __name__ == '__main__':
    executor.start_polling(dp)
