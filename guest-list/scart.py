import time
from datetime import date

#get current time
t = time.localtime()
current_time = time.strftime("%H:%M", t)
print(current_time)

#get current date
today = date.today()
print("Today's date:", today)