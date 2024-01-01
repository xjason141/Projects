#app to register guests at a guardhouse
from module import Guests
import csv
import os

#run this if csv file does not exist
def initial():
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
    with open('place.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, insert.keys())
        writer.writeheader()
        writer.writerow(insert)

    return f'Welcome {guest.name} u sucker. You arrived here at {guest.time} on {guest.date} for {guest.reason}. Your vehicle number is {guest.plate}'

#run this if csv exist or to update rows in existing csv. CODE BELOW NEEDS FIXING
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

#check if csv file exists
exist = os.path.isfile('place.csv')

if exist == False:
    initial() #run this if csv does not exist
    print('file created. guest has been added')
else:
    updater() #run this if csv exists/to update rows in existing csv
    print('csv updated')