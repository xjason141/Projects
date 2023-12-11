#app to register guests at a guardhouse
import datetime

def arrive():
    #gather info on guest
    date = input('Date: ')
    time = input('Time: ')
    name = input('Name: ')
    plate = input('Plate: ')
    reason = input('Reason: ')

    print(f'Guest {name} has been registered in the database')

arrive()
