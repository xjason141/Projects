#to get rows from csv

import csv

with open('guest-list/place.csv') as file:
    
    #syntax below reads everything in csv file
    read = csv.reader(file)
    for stuff in read:
        print(stuff)


