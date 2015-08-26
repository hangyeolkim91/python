import datetime
import time

timed = datetime.timedelta(seconds=1)
today = datetime.datetime.now()
while True:

    print(today.strftime('%Y-%m-%d %H:%M:%S'))
    today -=timed
    time.sleep(1)