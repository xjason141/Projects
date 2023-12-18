#app to register guests at a guardhouse
from module import Guests
import datetime

#attr list = date, time, name, id,  plate, reason

test_list = []

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

    #transfer guest info into a dict and appended into a list
    insert = guest.asdict()
    test_list.append(insert)

    return f'Welcome {guest.name} u sucker. You arrived here at {guest.time} on {guest.date} for {guest.reason}. Your vehicle number is {guest.plate}'

print(people())
print(test_list)