import requests
import time
from plyer import notification


def get_current_block_height():
    response = requests.get("https://blockchain.info/q/getblockcount")
    return response.json()


def main():
    while True:
        current_height = get_current_block_height()
        print(f"Current Bitcoin Block Height: {current_height}")
        # Notify every time it fetches the data
        notification.notify(
            title='Bitcoin Block Height Update',
            message=f'Current Bitcoin Block Height: {current_height}',
            app_icon=None,  # Path to an .ico file if you want a custom icon
            timeout=10  # Notification duration in seconds
        )
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    main()
