#!/usr/bin/python3

from module import Guests
import datetime
import json
import os

curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


#updates/creates the guest list
def updater(filepath):     
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
    # if file exists, update only
    if os.path.exists(filepath):
        y = Guests.asdict(guest)

        with open(filepath, 'r') as f:
            data = json.load(f)
            data['guests'].append(y)

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print('Guest updated.')
    
    # if file not exists, create new file and update
    else:
        y = {'guests': [Guests.asdict(guest)]}

        with open(filepath, 'w') as guest_json:
            json.dump(y, guest_json, indent=2)
        print('New file created. Guest updated.')


#retrieve guest info from guests.json
def retrieve(filepath):
    with open(filepath, 'r') as file:
        x = input('ID: ')
        try:
            data = json.load(file)
            guest_data = data['guests']
            count = 0
            
            #transform user input to int. raises ValueError if not int
            int(x)

            #check user input length
            if len(x) != 12:
                raise Exception

            for guests in guest_data:
                if x == guests['id']:
                    print('Guest info:\n{}\n{}\n{}\n{}\n{}'.format(guests['date'], guests['name'],guests['id'], guests['plate'], guests['address']))
                else:
                    count += 1
                if count == len(guest_data):
                    print('Guest does not exist')

        except ValueError as error:
            print(type(error).__name__ + ': Invalid ID. ID should only be numbers.')
            retrieve(filepath)
        except Exception:
            print('ID must include only 12 characters.')
            retrieve(filepath)


# runs everything
def main(filepath):
    to_do = ('1: Update', '2: Retrieve')
    joined = (', '.join(to_do))
    print(joined)
    try:
        decision = int(input("Press 1 or 2: "))
        while decision !=1 and decision !=2:
            print('Invalid option. Please choose either option 1 or 2.\n' + joined)
            decision = int(input("Press 1 or 2: "))
        if decision == 1:
            updater(filepath)
        else:
            retrieve(filepath)
            
    except ValueError as error:
        print(type(error).__name__ + ': Please choose either option 1 or 2.')
        main(filepath)


filepath = 'guest-list/guests.json'
if __name__ == '__main__':
    main(filepath)