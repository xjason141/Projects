from module import Guests
import datetime
import json
from pathlib import Path

#try using json instead of csv

curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


#initial start up if json file does not exist
def initial(filepath):
    print("Please register here")
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: ' ),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        address=input('Address: ')
        )
    
    #prepare to load into json
    # y = {'guests': [Guests.asdict(guest)]}
    # with open(filepath, 'w') as guest_json:
    #     json.dump(y, guest_json, indent=2)
    print(f'{guest.name} arrived at {guest.time} on {guest.date}')

x = 'guest-list/guests.json'
initial(x)