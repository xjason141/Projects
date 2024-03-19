from module import Guests
import datetime
import json

#try using json instead of csv

curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


def initial(): #initial start up if json file does not exist
    print("Please register here")
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: ' ),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        )
    
    #prepare to load into json
    y = {'guests': [Guests.asdict(guest)]}
    with open('guest-list/guests.json', 'w') as guest_json:
        json.dump(y, guest_json, indent=2)

    # print(f'{guest.name} arrived at {guest.time} on {guest.date}')


def updater():#run this if json file exists      
    print("Please register here")
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: ' ),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        )
    
    y = Guests.asdict(guest)
    
    #load json 1st, then dump into json
    with open('guest-list/guests.json', 'r') as f:
        data = json.load(f)
        data['guests'].append(y)

    with open('guest-list/guests.json', 'w') as f:
        json.dump(data, f, indent=2)


def retrieve():#retrieve guest info from guests.json
    with open('guest-list/guests.json') as file:
        data = json.load(file)
        pass

def run():
    x = int(input('Number: '))

    if x == 1:
        initial()
    if x == 2:
        updater()

run()


