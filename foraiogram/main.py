import asyncio
import logging
import sys, os
#
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# MongoDB ulanish
client = MongoClient(os.getenv("MONGO_DB"))
db = client["myDatabase"]
collection = db["messages"]

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    collection.insert_one({"user_id": message.from_user.id, "message": message.text})
    await message.reply("Salom! Sizning xabaringiz saqlandi MongoDB’ga!")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())