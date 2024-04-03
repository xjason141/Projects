import json

x = 'guest-list/guests.json'
y = 'email/car_sales.json'


with open(x, 'r') as file:
    data = json.load(file)
    guest_info = data['guests']

    guest_id = input('ID: ')
    for item in guest_info:
        if guest_info == item['id']:
            guest_id = item['id']
    
        getting = '{}\n{}\n{}\n{}\n{}'.format(item['name'], item['date'], item['time'], item['id'], item['plate'])

print(getting)