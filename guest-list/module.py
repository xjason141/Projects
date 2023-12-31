#create class for guests

class Guests: #class name must always start with a capital letter
    def __init__(self, date, time, name, id, plate, reason):
        self.date = date
        self.time = time
        self.name = name
        self.id = id
        self.plate = plate
        self.reason = reason

    def asdict(self): #method is to enable guest info to become a dict
        return {'date': self.date, 'time': self.time, 'name': self.name, 'id': self.id, 'plate': self.plate, 'reason': self.reason}
    