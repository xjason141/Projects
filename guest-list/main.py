from module import Guests
import datetime
import json
import os


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
    y = {'guests': [Guests.asdict(guest)]}
    with open(filepath, 'w') as guest_json:
        json.dump(y, guest_json, indent=2)
    print(f'{guest.name} arrived at {guest.time} on {guest.date} going to {guest.address}')


#run this if json file exists 
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
    
    y = Guests.asdict(guest)

    with open(filepath, 'r') as f:
        data = json.load(f)
        data['guests'].append(y)

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


#retrieve guest info from guests.json
def retrieve(pathfile):
    with open(pathfile, 'r') as file:
        data = json.load(file)
        guest_data = data['guests']
        x = int(input('ID: '))

        for guests in guest_data:
            if x == guests['id']:
                x = guests['id']
                print('{}\n{}\n{}\n{}\n{}'.format(guests['date'], guests['name'], guests['id'], guests['plate'], guests['address']))


def options(filepath):
    if os.path.exists(filepath):
        updater(filepath)
        print('Updating file')
    else:
        initial(filepath)
        print('New file created')


def main(filepath):
    one = ('Opt 1: Update')
    two = ('Opt 2: Retrieve')
    print(one + ', ' + two)
    decision = int(input("Press 1 or 2: "))

    if decision == 1:
        options(filepath)
    else:
        retrieve(filepath)


filepath = 'guest-list/guests.json'
if __name__ == '__main__':
    main(filepath)
