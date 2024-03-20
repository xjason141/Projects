import cars
import locale
import json


"""Loads the contents of filename as a JSON file."""
with open('email/car_sales.json') as f:
    data = json.load(f)
    newlist = []
    for item in data:
        newlist.append(item['total_sales'])
    newlist.sort()
    x = newlist[-1]
    
    for item in data:
        if item['total_sales'] == x:
            most = item['car']['car_model']
            print(most)

  
    # for stuff in data:
    #     print(stuff['total_sales'])
        
