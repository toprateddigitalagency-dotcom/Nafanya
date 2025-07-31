from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7629814043:AAEK_tA9lDRaMKKOQspcZj1a9URfC6eED60"

# Простейшие команды
def get_status():
    return "Gemini: Да\nBinance: Да\nБаланс: BTC 0.05, USDT 15"

def get_balance():
    return "Баланс Binance: BTC 0.05, USDT 15"

def get_logs():
    return "Последние действия:\n- [INFO] Запуск ядра\n- [ALERT] Баланс низкий"

def analyze_text(query):
    return f"Анализ Gemini: {query} → Пример ответа."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        if text == "/статус":
            reply = get_status()
        elif text == "/баланс":
            reply = get_balance()
        elif text == "/последние":
            reply = get_logs()
        elif text.startswith("/анализ"):
            query = text.replace("/анализ", "").strip()
            reply = analyze_text(query)
        else:
            reply = "Команды:\n/статус\n/баланс\n/последние\n/анализ <запрос>"

        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                      data={"chat_id": chat_id, "text": reply})

    return {"ok": True}

@app.route("/")
def home():
    return "Nafanya Bot is running!"
