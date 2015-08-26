import datetime
import time
import random

dt = datetime.datetime.strptime("20150809","%Y%m%d")
td_m = datetime.timedelta(minutes=1)
td_d = datetime.timedelta(days=1 )

while True:

    time.sleep(1)
    filen= dt.strftime("%Y%m%d")
    filen +='_DATA'

    data = []

    dt_next = dt + td_d

    while dt < dt_next-td_m :
        rn1 = random.randrange(1000,10000)
        rn2 = random.randrange(1000,10000)
        rn3 = random.randrange(1000,10000)
        rn4 = random.randrange(1000,10000)
        #time.sleep(1)
        dt += td_m
        temp = dt.strftime('%Y%m%d%H%M')+','+str(rn1)+','+str(rn2)+','+str(rn3)+','+str(rn4)+'\n'
        #print(temp)
        data.append(temp)

    with open(filen,'w') as f:
        f.writelines(data)

    dt = dt_next

