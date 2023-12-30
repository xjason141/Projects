#app to register guests at a guardhouse
from module import Guests
import csv

def initial(): #need only to be launched once the first time to create a new csv file
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

    #transform guest info into a dict
    insert = guest.asdict()

    #transfer guest info to place.csv
    with open('place.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=insert)
        writer.writeheader()
        writer.writerows(insert)

    file.close()

    return f'Welcome {guest.name} u sucker. You arrived here at {guest.time} on {guest.date} for {guest.reason}. Your vehicle number is {guest.plate}'

print(initial())

#try to use if statement. if csv exist, update rows. else create new csv 
def updater():
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

    #transform guest info into a dict
    insert = guest.asdict()

    #transfer guest info to place.csv
    with open('place.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=insert)
        writer.writeheader()
        writer.writerows(insert)

    file.close()

    return f'Welcome {guest.name} u sucker. You arrived here at {guest.time} on {guest.date} for {guest.reason}. Your vehicle number is {guest.plate}'