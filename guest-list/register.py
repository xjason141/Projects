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

#run this if csv exist or to update rows in existing csv. SYNTAX TO UPDATE CSV FILE NEEDS FIXING.
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

    #new guest info
    new_info = list(insert.values())

    #transfer guest info to place.csv
    with open('place.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_info)

#check if csv file exists
exist = os.path.isfile('place.csv')

if exist == False:
    initial()
    print('file created. guest has been added')
else:
    updater()
    print('csv updated')