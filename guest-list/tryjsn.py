from module import Guests
import datetime
import json

#try using json instead of csv

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
    
    #prepare to load into json
    y = {'guests': [Guests.asdict(guest)]}
    with open('guest-list/guests.json', 'w') as guest_json:
        json.dump(y, guest_json, indent=2)

    # print(f'{guest.name} arrived at {guest.time} on {guest.date}')
        
def updater():
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
    
    #prepare to load into json
    y = guest.asdict()
    with open('guest-list/guests.json') as guest_json:
        pass


    with open('guest-list/guests.json', 'a') as f:
        pass
def retrieve():
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


