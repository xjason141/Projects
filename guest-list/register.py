#app to register guests at a guardhouse
from module import Guests
import csv

def people():
    print("Please register here")

    #guests info here (date, time, plate, name, id, reason)
    guest = Guests(
        date=input('Date: '),
        time=input('Time: '),
        name=input('Name: '),
        id=input('ID: '),
        plate=input('Plate: '),
        reason=input('Reason: '),
        )

    #transform guest info into a dict
    insert = guest.asdict()

    #appending guest dict into place.csv
    with open('place.csv', 'a+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=insert.keys())
        writer.writeheader()
        writer.writerow(insert)

    file.close()
    
    return f'Welcome {guest.name} u sucker. You arrived here at {guest.time} on {guest.date} for {guest.reason}. Your vehicle number is {guest.plate}'

print(people())