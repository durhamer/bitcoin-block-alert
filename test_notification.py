import os


def notify(title, message):
    script = f'display notification "{message}" with title "{title}"'
    os.system(f"osascript -e '{script}'")


if __name__ == "__main__":
    # Direct test of the notification
    notify('Test Notification',
           'This is a direct test of the macOS notification system.')
