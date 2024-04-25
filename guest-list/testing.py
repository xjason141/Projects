from module import Guests
import datetime
import json
import os

curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')

def retrieve(pathfile):
    with open(pathfile, 'r') as file:
        try:
            data = json.load(file)
            guest_data = data['guests']
            x = int(input('ID: '))

            if len(str(x)) != 12:
                raise Exception

            for guests in guest_data:
                if x == guests['id']:
                    x = guests['id']
                    print('Guest info:\n{}\n{}\n{}\n{}\n{}'.format(guests['date'], guests['name'], guests['id'], guests['plate'], guests['address']))
        except ValueError as error:
            print(type(error).__name__ + ': Invalid ID.')
        except Exception:
            print('ID must include only 12 characters.')


filepath = 'guest-list/guests.json'
if __name__ == '__main__':
    retrieve(filepath)