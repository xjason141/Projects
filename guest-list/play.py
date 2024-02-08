#creating checker func.
#checks if guest exists or not in csv file.
#if guest exists, return/print entire info on guest.
#checker() not yet completed. still in creation phase.

from module import Guests
import datetime
import csv
import os

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

    print('success')

#checker func
def checker():
    id = input("ID: ").capitalize()

    exist = []
    x = dict(exist)
    with open('guest-list/place.csv') as file:
        reader = csv.reader(file, delimiter=',')

        next(reader) #tskips the header

        for row in reader:
            exist.append(row)
    
    if id in str((exist)):
        print(x)
        print(exist)
    else:
        print('not here')

checker()