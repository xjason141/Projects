#bug fix has not been merged with main.py. PLEASE REFER NUMS.PY FIRST BEFORE MERGING.

from module import Guests
import datetime
import json
import os

curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')

# y = input("should be num here: ")

# if isinstance(int(y), int) == True:
#     print('is int')
# else:
#     print('not int')

# l = isinstance(int(y), int)

def initial(filepath):
    print("Please register here")
    # try:
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: ' ),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        address=input('Address: ')
        )
    
    #     if len(str(guest.id)) != 12:
    #         raise Exception
        
    #     # prepare to load into json
    y = {'guests': [Guests.asdict(guest)]}
    with open(filepath, 'w') as guest_json:
        json.dump(y, guest_json, indent=2)
    print('New file created. Guest updated.')     

    # except ValueError as error:
    #     print(type(error).__name__ + ': Invalid ID.')
    # except Exception:
    #     print('ID must include only 12 characters.')


def updater(filepath):
    print("Please register here")
    # try:
    guest = Guests(
            date=curr_date,
            time=curr_time,
            name=input('Name: ').capitalize(),
            id=input('ID: ' ),
            plate=input('Plate: ').upper(),
            reason=input('Reason: ').capitalize(),
            address=input('Address: ')
            )
        
        #ensure that guest.id is int
        # id_check = int(guest.id)
        # if isinstance(id_check, int) == False:
        #     raise ValueError

        # if len(guest.id) != 12:
        #     raise Exception
    y = Guests.asdict(guest)

    with open(filepath, 'r') as f:
        data = json.load(f)
        data['guests'].append(y)

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print('Guest updated.')
    # print(Guests.asdict(guest))

    # except ValueError as error:
    #     print(type(error).__name__ + ': Invalid ID.')
    # except Exception:
    #     print('ID must include only 12 characters.')

filepath = 'guest-list/guests.json'
if __name__ == '__main__':
    updater(filepath)
