#app to register guests at a guardhouse
from module import Guests
import datetime

#attr list = date, time, name, plate, reason

def people():
    print("Please register here")

    #guests info here (date, time, plate, name, id, reason)
    guest = Guests(
        date=input('Date: '),
        time=input('Time: '),
        name=input('Name: '),
        id=input('ID: '),
        plate=input('Plate: '),
        reason=input('Reason: '),
        )

    return f'Welcome {guest.name} u sucker. You arrived here at {guest.time} on {guest.date} for {guest.reason}. Your vehicle number is {guest.plate}'

print(people())




    
