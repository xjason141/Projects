from module import Guests
import datetime
import json

#try using json instead of csv

curr_time = datetime.datetime.now().strftime('%H:%M')
curr_date = datetime.datetime.now().strftime('%d-%b-%Y')


#initial start up if json file does not exist
def initial(filepath):
    print("Please register here")
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: ' ),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        )
    
    #prepare to load into json
    y = {'guests': [Guests.asdict(guest)]}
    with open(filepath, 'w') as guest_json:
        json.dump(y, guest_json, indent=2)
    # print(f'{guest.name} arrived at {guest.time} on {guest.date}')


#run this if json file exists 
def updater(filepath):     
    print("Please register here")
    guest = Guests(
        date=curr_date,
        time=curr_time,
        name=input('Name: ').capitalize(),
        id=input('ID: ' ),
        plate=input('Plate: ').upper(),
        reason=input('Reason: ').capitalize(),
        )
    
    y = Guests.asdict(guest)
    
    #load json 1st, then dump into json
    with open(filepath, 'r') as f:
        data = json.load(f)
        data['guests'].append(y)

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


#retrieve guest info from guests.json
def retrieve(pathfile):
    with open(pathfile, 'r') as file:
        data = json.load(file)
        guest_data = data['guests']
        x = input('Name: ').capitalize()

        for guests in guest_data:
            if x == guests['name']:
                x = guests['name']
                print('{}\n{}\n{}\n{}'.format(guests['date'], guests['name'], guests['id'], guests['plate']))


filepath = 'guest-list/guests.json'
retrieve(filepath)