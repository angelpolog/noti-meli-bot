from flask import Flask, request
import os
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route("/")
def home():
    return "🤖 Bot de Mercado Libre funcionando"

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    message = data.get("message", "Notificación de Mercado Libre")
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        })
    return {"status": "ok"}
