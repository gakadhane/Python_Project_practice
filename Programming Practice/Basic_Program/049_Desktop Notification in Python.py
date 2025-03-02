import time

from plyer import notification  # pip install plyer

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Alert !!",
            message="Take a break",
            timeout=10
        )
        time.sleep(1000)
        break
