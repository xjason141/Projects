from module import Guests
import datetime
import csv
import os

#get current date and time
curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


def updater():
    temp = []
    print("Please register here")

    global guest
    #guests info here (date, time, plate, name, id, reason)

    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: '),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        )

    # print(guest.name)
    #transform guest info into a dict
    insert = guest.asdict()

    for v in insert.values():
        x = v.split()
        temp.append(x)
    
    if guest.name in str(temp):
        print(guest.name + ' is in here')
    else:
        #new guest info
        new_info = list(insert.values())

        #transfer guest info to place.csv
        with open('guest-list/place.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_info)

        print(f'{guest.name} arrived at {guest.time} on {guest.date}')

updater()
