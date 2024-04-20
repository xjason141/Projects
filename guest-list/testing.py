from module import Guests
import datetime
import json
import os


curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


#initial start up if json file does not exist
def initial(filepath):
    print("Please register here")

    try:
        guest = Guests(
            date=curr_date,
            time=curr_time,
            name=input('Name: ').capitalize(),
            id=input('ID: ' ),
            plate=input('Plate: ').upper(),
            reason=input('Reason: ').capitalize(),
            address=input('Address: ')
            )
        if len(str(guest.id)) < 12:
            print('ID too short')
        if len(str(guest.id)) > 12:
            print('ID too long')
        #prepare to load into json
            # y = {'guests': [Guests.asdict(guest)]}
            # with open(filepath, 'w') as guest_json:
            #     json.dump(y, guest_json, indent=2)    
    except ValueError as error:
        print(type(error).__name__ + ': Invalid ID.')
    
    y = {'guests': [Guests.asdict(guest)]}
    with open(filepath, 'w') as guest_json:
        json.dump(y, guest_json, indent=2)    



filepath = 'guest-list/guests.json'
if __name__ == '__main__':
    initial(filepath)