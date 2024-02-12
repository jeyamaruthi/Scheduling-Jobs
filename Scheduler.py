import schedule
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime


def sleep_reminder():
    print("Stop playing video games indefinitely")
    print("You are a grown-up adult with a lot of responsibilities!")
    print("Go to Bed! you ****")

schedule.every().day.at("21:15").do(sleep_reminder)

while True:
    schedule.run_pending()
    time.sleep(1)

