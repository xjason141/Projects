#create class for guests

class Guests: #class name must always start with a capital letter
    def __init__(self, date, time, name, plate, reason):
        self.date = date
        self.time = time
        self.name = name
        self.plate = plate
        self.reason = reason