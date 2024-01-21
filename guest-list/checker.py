import csv

#check if guest info exist in csv
def check():
    check = []

    with open('guest-list/place.csv', 'r') as file:

        read = csv.reader(file)

        #skip the header in csv
        next(file)
        
        for stuff in read:
            check.append(stuff)

        #checking
        if 'Didi' in str(check):
            print(check[0][0], check[0][2]) #get value from check using index
        else:
            print('error')

    #print(check)

check()
