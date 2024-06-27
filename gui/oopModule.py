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
            # print(type(error).__name__ + ': Invalid ID.')
            sys.exit(type(error).__name__ + ': Invalid ID.')
        except Exception:
            # print('ID must include only 12 characters.')
            sys.exit('ID must include only 12 characters.')

    
    #transform guest info into dict
    def asdict(self):
        transform = {'date': self.date, 'time': self.time, 'name': self.name, 'id': self.id, 'plate': self.plate, 'reason': self.reason, 'address': self.address}
        to_dict = {'guests': transform}
        return to_dict
        


x = Guests()
print(x.asdict())