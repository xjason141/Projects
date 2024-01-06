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
        date=input('date: ' + curr_date),
        time=input('Time: ' + curr_time),
        name=input('Name: '),
        id=input('ID: '),
        plate=input('Plate: '),
        reason=input('Reason: '),
        )

    #transform guest info into a dict
    insert = guest.asdict()

    #appending guest dict into place.csv
    with open('place.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, insert.keys())
        writer.writeheader()
        writer.writerow(insert)

#run this if csv exist or to update rows in existing csv.
def updater():
    print("Please register here")

    #guests info here (date, time, plate, name, id, reason)
    guest = Guests(
        date=curr_date,
        time=curr_time,
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
