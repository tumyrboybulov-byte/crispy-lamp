import os
import telebot

BOT_TOKEN = os.environ.get("8726750443:AAEyVRTAaYLaKIn7vr0TT1gDuo8e8xjiGto")
CHAT_ID = os.environ.get("5560619845")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is alive.")

# Эндпоинт для приёма куки
@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"echo: {message.text}")

if __name__ == "__main__":
    bot.infinity_polling()