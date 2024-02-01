#chceker func 1st
from module import Guests
import datetime
import csv
import os

curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')

def initial(): #run this if csv file does not exist
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


def checker():
    id = input("ID: ")
    #create input to check if id exist in csv.
    #if exist, run update() func
    #if not, run initial()
    #checker() not yet completed. still in creation phase.

    exist = []
    with open('guest-list/place.csv') as file:
        reader = csv.reader(file, delimiter=',')

        next(reader) # this syntax skips the header

        for row in reader:
            exist.append(row)
    
    if id in str(exist):
        print('the id is in here')
    else:
        print('does not exist')

    

checker()