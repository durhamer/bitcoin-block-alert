import requests
import time
import os


def get_current_block_height():
    response = requests.get("https://blockchain.info/q/getblockcount")
    return response.json()


def notify(title, message):
    # Using terminal-notifier to send a sticky notification
    os.system(
        f'terminal-notifier -title "{title}" -message "{message}" -sound default -sticky')


def main():
    current_height = get_current_block_height()
    print(f"Current Bitcoin Block Height: {current_height}")

    target_height = int(input("Enter the target block height: "))

    while True:
        current_height = get_current_block_height()
        print(f"Current Bitcoin Block Height: {current_height}")
        if current_height >= target_height:
            notify('Bitcoin Block Height Alert',
                   f'The current block height {current_height} has reached or surpassed the target of {target_height}.')
            break
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    main()
