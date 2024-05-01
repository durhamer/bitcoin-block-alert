import configparser
import requests
import time


def get_current_block_height():
    response = requests.get("https://blockchain.info/q/getblockcount")
    return response.json()


def send_telegram_message(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()


def main():
    # Load configuration
    config = configparser.ConfigParser()
    config.read('config.ini')
    bot_token = config['telegram']['bot_token']
    chat_id = config['telegram']['chat_id']

    # Display the current block height before asking for the target height
    current_height = get_current_block_height()
    print(f"Current Bitcoin Block Height: {current_height}")

    target_height = int(input("Enter the target block height: "))
    # Prompt user to enter a note
    note = input("Enter a note for this target block height: ")

    while True:
        current_height = get_current_block_height()
        print(f"Current Bitcoin Block Height: {current_height}")
        if current_height >= target_height:
            # Include the user's note in the message
            message = f'The current block height {current_height} has reached or surpassed the target of {target_height}. Note: {note}'
            send_telegram_message(bot_token, chat_id, message)
            break
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    main()
