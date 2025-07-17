from flask import Flask, request
from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_B_TOKEN = os.getenv("BOT_B_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_B_TOKEN)
app = Flask(__name__)

@app.route('/send', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('message')
    if message:
        bot.send_message(chat_id=CHAT_ID, text=f"📨 Получено от Bot A: {message}")
        return {'status': 'ok'}, 200
    return {'error': 'No message provided'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
