from module import Guests
import datetime
import json
import os

def retrieve(filepath):
    with open(filepath, 'r') as file:
        try:
            data = json.load(file)
            guest_data = data['guests']
            count = 0

            x = input('ID: ')
            if int(x) == False:
                raise ValueError

            if len(x) != 12:
                raise Exception
            
            for guests in guest_data:
                if x == guests['id']:
                    x = guests['id']
                    print('Guest info:\n{}\n{}\n{}\n{}\n{}'.format(guests['date'], guests['name'],guests['id'], guests['plate'], guests['address']))
                    return x
                else:
                    count += 1
                if count == len(guest_data):
                    print('Guest does not exist')
                    # to_update = input('Update the guest? Yes or No? ').lower()
                    # if to_update == 'yes':
                    #     updater(filepath, Guests(id=x))
                    # else:
                    #     continue

        except ValueError as error:
            print(type(error).__name__ + ': Invalid ID.')
        except Exception:
            print('ID must include only 12 characters.')

filepath = 'guest-list/guests.json'
if __name__ == '__main__':
    retrieve(filepath)