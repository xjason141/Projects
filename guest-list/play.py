from module import Guests
import datetime
import csv
import json
#creating checker func.
#checks if guest exists or not in csv file.
#if guest exists, return/print entire info on guest.
#checker() not yet completed. still in creation phase.

curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


def initial():
    print("Please register here")

    #guests info here (date, time, plate, name, id, reason)
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: ' ),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        )
    # print('success')

    #transform guest info into a dict
    insert = guest.asdict()

    #appending guest dict into place.csv
    with open('guest-list/place.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, insert.keys())
        writer.writeheader()
        writer.writerow(insert)

    print(f'{guest.name} arrived at {guest.time} on {guest.date}')

#checks if ID exists in csv
def checker():
    id = input("ID: ").capitalize()

    exist = []
    with open('guest-list/place.csv') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader) #skips the header
        for k in file:
            print(k['name'])

checker()
