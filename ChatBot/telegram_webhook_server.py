import sys
import asyncio
import requests
from flask import Flask, request, jsonify

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

TELEGRAM_TOKEN = "7789235645:AAF-VV0iSGFxkchF7iinGRJOmtEyLe-zwtg"
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

app = Flask(__name__)

def send_telegram_message(chat_id, text):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        response = requests.post(url, json=payload, timeout=5)
        print(f"Risposta Telegram: {response.json()}")
    except Exception as e:
        print(f"Errore invio Telegram: {e}")

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    print("Ricevuto update:", update)
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")
    elif "callback_query" in update:
        chat_id = update["callback_query"]["message"]["chat"]["id"]
        text = update["callback_query"]["data"]
    else:
        return jsonify({"status": "ignorato"}), 200

    print(f"Messaggio da Telegram: chat_id={chat_id}, text='{text}'")
    rasa_payload = {"sender": str(chat_id), "message": text}
    print(f"Inviando a Rasa: {rasa_payload}")
    try:
        rasa_response = requests.post(RASA_URL, json=rasa_payload, timeout=10)
        print(f"Risposta Rasa (status {rasa_response.status_code}): {rasa_response.text}")
        if rasa_response.status_code == 200:
            rasa_messages = rasa_response.json()
            for i, msg in enumerate(rasa_messages):
                if "text" in msg:
                    print(f"Inviando a Telegram (messaggio {i}): {msg['text']}")
                    send_telegram_message(chat_id, msg["text"])
    except Exception as e:
        print("ERRORE durante la comunicazione con Rasa:", e)

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    webhook_url = "https://departed-urgent-borrowing.ngrok-free.dev/webhook"
    set_webhook_url = f"{TELEGRAM_API}/setWebhook?url={webhook_url}"
    response = requests.get(set_webhook_url).json()
    print("Set webhook response:", response)
    app.run(host="0.0.0.0", port=5000, debug=False)