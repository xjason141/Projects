import json



def retrieve(pathfile):
    with open(pathfile, 'r') as file:
        data = json.load(file)
        guest_data = data['guests']
        x = input('Name: ').capitalize()

        for guests in guest_data:
            if x == guests['name']:
                x = guests['name']
                print('{}\n{}'.format(guests['id'], guests['date']))


x = 'guest-list/guests.json'
retrieve(x)