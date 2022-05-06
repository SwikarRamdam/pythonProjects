from email import message
from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Passport Form",
            message = "Go to cyber to fill passport form and then go to bank to verify connect IPS",
            app_icon = "think.png",
            timeout = 5)
        time.sleep(20)
        