import datetime
import json
import os
import sys

class Guests:
    def __init__(self):
        #set current time and date
        curr_time = datetime.datetime.now().strftime('%H:%M')
        curr_date = datetime.datetime.now().strftime('%d-%b-%Y')

        #takes input for guest info
        try:
            self.date = curr_date
            self.time = curr_time
            self.name = input('Name: ').capitalize()
            self.id = int(input('ID: '))
            self.plate = input('Plate Number: ')
            self.reason = input('Reason: ')
            self.address = input('Address: ')

            #check if self.id is not int
            if self.id == False:
                raise ValueError
            # if len(str(self.id)) != 12:
            #     raise Exception
            
        except ValueError as error:
            sys.exit(type(error).__name__ + ': Invalid ID.')
        except Exception:
            sys.exit('ID must include only 12 characters.')

    
    #transform guest info into dict
    def main(self):
        transform = {'date': self.date, 'time': self.time, 'name': self.name, 'id': self.id, 'plate': self.plate, 'reason': self.reason, 'address': self.address}
        to_dict = {'guests': [transform]}

        with open(filepath, 'w') as writer:
            json.dump(to_dict, writer, indent=2)
        return 'New file created. Guest has been registered.'
    

class Updater(Guests):
    def update(self):
        to_dict = {'date': self.date, 'time': self.time, 'name': self.name, 'id': self.id, 'plate': self.plate, 'reason': self.reason, 'address': self.address}

        with open(filepath, 'r') as f:
            data = json.load(f)
            data['guests'].append(to_dict)

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return 'success'

class mainApp():
    def do(self):
        Updater().update()
        return 'yessir'

        

filepath = 'guest-list/new_guest.json'
if __name__ == '__main__':
    x = mainApp()
    print(x.do())