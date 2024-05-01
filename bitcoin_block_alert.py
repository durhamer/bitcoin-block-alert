from flask import Flask, request, jsonify
import requests
import configparser
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
BOT_TOKEN = config['telegram']['bot_token']
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

user_states = {}  # Track user states and data, including their notes


def get_current_block_height():
    response = requests.get("https://blockchain.info/q/getblockcount")
    return response.json()


def check_block_heights():
    current_height = get_current_block_height()
    alerts_to_remove = []
    for chat_id, user_info in user_states.items():
        if 'target_height' in user_info and current_height >= user_info['target_height']:
            send_telegram_message(
                chat_id,
                f"The current block height {current_height} has reached or surpassed your target of {user_info['target_height']} with note: '{user_info.get('note', 'No note provided')}'."
            )
            alerts_to_remove.append(chat_id)
    for chat_id in alerts_to_remove:
        del user_states[chat_id]


def send_telegram_message(chat_id, message):
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    requests.post(TELEGRAM_API_URL, data=payload)


def process_message(chat_id, text):
    if chat_id not in user_states:
        user_states[chat_id] = {"stage": "start"}

    if text == "/start":
        current_height = get_current_block_height()
        message = f"Current Bitcoin Block Height: {current_height}\nPlease enter your target block height and a note (e.g., '100000, call QIAN')."
        send_telegram_message(chat_id, message)
        user_states[chat_id] = {"stage": "awaiting_input"}
    elif user_states[chat_id]["stage"] == "awaiting_input":
        try:
            # Split input into target height and note
            target_height, note = text.split(',', 1)
            target_height = int(target_height.strip())
            note = note.strip()
            user_states[chat_id] = {"stage": "set",
                                    "target_height": target_height, "note": note}
            send_telegram_message(
                chat_id, f"Alert set for block height {target_height} with note: '{note}'. We will notify you once it reaches this height.")
        except ValueError:
            send_telegram_message(
                chat_id, "Please make sure to enter the target block height followed by a comma and your note.")


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    process_message(chat_id, text)
    return jsonify({'status': 'ok'}), 200


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    # Schedule to run every 10 minutes
    scheduler.add_job(check_block_heights, 'interval', minutes=1)
    scheduler.start()
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        scheduler.shutdown()  # Properly shut down the scheduler when the app stops
