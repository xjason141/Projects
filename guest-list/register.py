#app to register guests at a guardhouse
from module import Guests
import datetime
import csv
import os

#get current date and time
curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%y')

def initial(): #run this if csv file does not exist
    print("Please register here")

    #guests info here (date, time, plate, name, id, reason)
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: '),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        )
    
    #transform guest info into a dict
    insert = guest.asdict()

    #appending guest dict into place.csv
    with open('guest-list/place.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, insert.keys())
        writer.writeheader()
        writer.writerow(insert)

    print(f'{guest.name} arrived at {guest.time} on {guest.date}')

#run this if csv exist or to update rows in existing csv.
def updater():
    print("Please register here")

    #guests info here (date, time, plate, name, id, reason)
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: '),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        )

    #transform guest info into a dict
    insert = guest.asdict()

    #new guest info
    new_info = list(insert.values())

    #transfer guest info to place.csv
    with open('guest-list/place.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_info)

    print(f'{guest.name} arrived at {guest.time} on {guest.date}')

#check if csv file exists
exist = os.path.isfile('guest-list/place.csv')

if exist == False:
    initial()
    print('file created. guest has been added')
else:
    updater()
    print('csv updated')
