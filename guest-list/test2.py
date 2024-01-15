#to get rows from csv
import csv

check = []

with open('guest-list/place.csv', 'r') as file:
    
    #reader object
    read = csv.reader(file)

    #this syntax to skip the header in csv
    next(file)

    #append the rows in csv into a list
    for stuff in read:
        check.append(stuff)

    
    #checking
    if 'Didi' in str(check):
        print(check[0][0], check[0][2]) #get value from check using index
    else:
        print('error')

print(check)










