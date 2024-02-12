import schedule
import time
from win10toast import ToastNotifier

def job():
    toaster = ToastNotifier()
    toaster.show_toast("Sleep Reminder", "Stop playing video games!\nYou are a grown-up adult with responsibilities!\nGo to bed!", duration=10)

schedule.every().day.at("21:55").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
