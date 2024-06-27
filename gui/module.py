
import sys

class Guests:
    #set current time and date

    def __init__(self, date, time, name, id, plate, reason, address):
        try:
            self.date = date
            self.time = time
            self.name = name
            self.id = id
            self.plate = plate
            self.reason = reason
            self.address = address

            id_check = int(self.id)
            if isinstance(id_check, int) == False:
                raise ValueError
            if len(self.id) != 12:
                raise Exception
            
        except ValueError as error:
            # print(type(error).__name__ + ': Invalid ID.')
            sys.exit(type(error).__name__ + ': Invalid ID.')
        except Exception:
            # print('ID must include only 12 characters.')
            sys.exit('ID must include only 12 characters.')

    def asdict(self): #method is to enable guest info to become a dict
        return {'date': self.date, 'time': self.time, 'name': self.name, 'id': self.id, 'plate': self.plate, 'reason': self.reason, 'address': self.address}


    