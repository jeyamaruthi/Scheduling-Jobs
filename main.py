import schedule
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime


def job():
    print("Well Hello there")

### Some examples to use schedule ################

#Every 5 Seconds:
# schedule.every(5).seconds.do(job)

#Everyday at 8:47 PM
# schedule.every().day.at("20:47").do(job)

#Run every one to 5 seconds
# schedule.every(1).to(5).second.do(job)

##################################################

# Lets assign this job into a paramenter and cancel
# below using a condition

j1 = schedule.every(2).seconds.do(job)
c = 0

while True:
    schedule.run_pending()
    tm.sleep(1)
    c+=1
    if c==10:
        schedule.cancel_job(j1)
        break

@repeat(every(5).seconds, message = "hey")
@repeat(every(6).seconds, message = "Bye")
def job2(message):
    print("Lets use annotations:", message)

while True:
    schedule.run_pending()
    tm.sleep(1)

