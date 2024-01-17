from module import Guests
import datetime
import csv
import os

#get current date and time
curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


head = []
check = []


def initial(): #run this if csv file does not exist
    print("Please register here")

    #global insert
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

    print(insert)

initial()