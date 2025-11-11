import os
import telebot

# Берём токен из переменной окружения TOKEN (мы уже добавили её в Render)
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("Не задан TOKEN в переменных окружения")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def handle_start(message: telebot.types.Message):
    bot.send_message(
        message.chat.id,
        "Привет! Я жив и работаю на Render 🤖\n"
        "Напиши мне что-нибудь, а я повторю."
    )


@bot.message_handler(content_types=["text"])
def handle_text(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Ты написал: <b>{message.text}</b>")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
