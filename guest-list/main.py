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
        
        if len(str(guest.id)) != 12:
            raise Exception
        
        # prepare to load into json
        y = {'guests': [Guests.asdict(guest)]}
        with open(filepath, 'w') as guest_json:
            json.dump(y, guest_json, indent=2)
        print('New file created. Guest updated.')     
    except ValueError as error:
        print(type(error).__name__ + ': Invalid ID.')
    except Exception:
        print('ID must include only 12 characters.')

#run this if json file exists 
def updater(filepath):     
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
        
        if len(str(guest.id)) != 12:
            raise Exception
        
        y = Guests.asdict(guest)

        with open(filepath, 'r') as f:
            data = json.load(f)
            data['guests'].append(y)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print('Guest updated.')
    except ValueError as error:
        print(type(error).__name__ + ': Invalid ID.')
    except Exception:
        print('ID must include only 12 characters.')

#retrieve guest info from guests.json
def retrieve(filepath):
    with open(filepath, 'r') as file:
        try:
            data = json.load(file)
            guest_data = data['guests']
            count = 0
            x = int(input('ID: '))
            
            if len(str(x)) != 12:
                raise Exception
            
            for guests in guest_data:
                if x == guests['id']:
                    x = guests['id']
                    print('Guest info:\n{}\n{}\n{}\n{}\n{}'.format(guests['date'], guests['name'], 
                                                                    guests['id'], guests['plate'], guests['address']))
                else:
                    count += 1
                if count == len(guest_data):
                    print('no guest')
        except ValueError as error:
            print(type(error).__name__ + ': Invalid ID.')
        except Exception:
            print('ID must include only 12 characters.')

#create new json or update existing json
def options(filepath):
    if os.path.exists(filepath):
        updater(filepath)
    else:
        initial(filepath)
        
def main(filepath):
    to_do = ('Opt 1: Update', 'Opt 2: Retrieve')
    print(', '.join(to_do))

    decision = int(input("Press 1 or 2: "))
    try:
        while decision !=1 and decision !=2:
            print('Invalid option')
            decision = int(input("Press 1 or 2: "))
        if decision == 1:
            options(filepath)
        else:
            retrieve(filepath)
    except ValueError as error:
        print(type(error).__name__ + ': Please choose either option 1 or 2.')

filepath = 'guest-list/guests.json'
if __name__ == '__main__':
    main(filepath)
