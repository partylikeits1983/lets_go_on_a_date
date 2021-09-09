import time
import datetime

d = datetime.datetime(2021,9,11,16,30)
ptime = time.mktime(d.timetuple())

d1 = datetime.datetime(2021,9,11,16,30)
ctime = time.mktime(d1.timetuple())


def GoOnDate():
    if ptime == ctime:
        print("Works great! See you then!")
        
    elif ctime > ptime:
        print("let's meet a bit later at " + d1.strftime("%H:%M:%S"))
    
    else:
        print("That's a bit too early")
    
GoOnDate()
