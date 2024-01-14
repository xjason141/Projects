#to get rows from csv
from module import Guests
import csv

head = []
check = []

with open('guest-list/place.csv', 'r') as file:
    
    #syntax below reads everything in csv file
    read = csv.reader(file)
    head = next(file)

    for stuff in read:
        check.append(stuff)
    if "Dodo" in str(check):
        print('Dodo in here')
    else:
        print('Nothing here')




