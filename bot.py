import os
from aiogram import Bot, Dispatcher, executor, types

# Берём токен из переменной окружения TOKEN (мы её добавим в Render)
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("Не задан TOKEN в переменных окружения")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я жив и работаю на Render 🤖")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
