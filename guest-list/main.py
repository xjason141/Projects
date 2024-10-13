#!/usr/bin/python3

from module import Guests
import datetime
import json
import os


curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


#updates/creates the guest list
def main_register(filepath):     
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
    y = Guests.asdict(guest)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
            data['guests'].append(y)

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print('Guest updated.')
    
    # if file not exists, create new file and update
    else:
        guest_info = {'guests': [y]}
        with open(filepath, 'w') as guest_json:
            json.dump(guest_info, guest_json, indent=2)
        print('New file created. Guest updated.')


#retrieve guest info from guests.json
def retrieve(filepath):
    global to_update
    global mark
    to_update = []
    mark = 0
    with open(filepath, 'r') as file:
        to_check = input('ID: ')
        try:
            data = json.load(file)
            guest_data = data['guests']
            count = 0
            
            #transform user input to int. raises ValueError if not int
            int(to_check)

            #check user input length
            if len(to_check) != 12:
                raise Exception

            # main checking part of the function
            for guests in guest_data:
                # check if any id is similar to the one from user input. and decide whether to update the list or not 
                if to_check == guests['id']:
                    print('Guest info:\n{}\n{}\n{}\n{}\n{}'.format(guests['date'], guests['name'],guests['id'], guests['plate'], guests['address']))
                    to_update = [guests['name'], guests['id']]
                    mark = 0
                    decision(filepath)
                    return
                else:
                    count += 1
                if count == len(guest_data):
                    print('Guest does not exist.')
                    to_update = to_check
                    mark = 1
                    decision(filepath)

        except ValueError as error:
            print(type(error).__name__ + ': Invalid ID. ID should only be numbers.')
            retrieve(filepath)
        except Exception:
            print('ID must include only 12 characters.')
            retrieve(filepath)


# decide whether to update the list or not
def decision(filepath):
    choice = input('Do you want to register the guest? Y/N: ').upper()
    while choice != 'Y' and choice != 'N':
        print('Invalid choice')
        choice = input('Do you want to register the guest? Y/N: ').upper()
    # if guest exists and want to update, run exist_updater(filepath) 
    if choice == 'Y' and mark == 0:
        exist_updater(filepath)
    elif choice == 'Y' and mark == 1:
        non_exist_updater(filepath)
    else:
        print('Goodbye')


# to update the list if guest does not exist in the list
def non_exist_updater(filepath):
    # print('running non')
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=to_update,
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        address=input('Address: ')
        )
    
    y = Guests.asdict(guest)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
            data['guests'].append(y)

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print('Guest updated.')


# to update the list if guest exist. guest's name and id will be retrieved from retrieve(filepath). no need for user input
def exist_updater(filepath):
    # print('running exist')
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=to_update[0], #retrieved from retrieve(filepath)
        id=to_update[1], #retrieved from retrieve(filepath)
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        address=input('Address: ')
        )

    y = Guests.asdict(guest)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
            data['guests'].append(y)

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print('Guest updated.')


# runs everything
def main(filepath):
    to_do = ('1: Register', '2: Retrieve')
    joined = (', '.join(to_do))
    print(joined)
    try:
        decision = int(input("Press 1 or 2: "))
        while decision !=1 and decision !=2:
            print('Invalid option. Please choose either option 1 or 2.\n' + joined)
            decision = int(input("Press 1 or 2: "))
        if decision == 1:
            main_register(filepath)
        else:
            retrieve(filepath)
            
    except ValueError as error:
        print(type(error).__name__ + ': Please choose either option 1 or 2.')
        main(filepath)

# set filepath and run script
filepath = 'guest-list/guests.json'
if __name__ == '__main__':
    main(filepath)