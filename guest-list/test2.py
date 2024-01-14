#to get rows from csv
import csv

head = []
check = []

with open('guest-list/place.csv', 'r') as file:
    
    #reader object
    read = csv.reader(file)

    #this syntax to skip the header in csv
    head = next(file)

    #append the rows in csv into a list
    for stuff in read:
        check.append(stuff)
    
    #checking
    if 'Dodo' in str(check):
        print('test complete')
    else:
        print('error')

#code below does not work. needs fixing
def create():
    if exist == False:
        initial()
        print('file created. guest has been added')
    else:
        with open('guest-list/place.csv', 'r') as file:
    
        #reader object
        read = csv.reader(file)

        #this syntax to skip the header in csv
        head = next(file)

        #append the rows in csv into a list
        for stuff in read:
            check.append(stuff)
    
        #checking
        if guest.name() in str(check):
            print(guest.name() + ',' + guest.id())
        else:
            #print('error')
            updater()
            print('csv updated')







