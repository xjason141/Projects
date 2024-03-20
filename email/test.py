import cars
import locale
import json


"""Loads the contents of filename as a JSON file."""
with open('email/car_sales.json') as f:
    data = json.load(f)
    newl = []
    for cars in data:
        newl.append(cars['total_sales'])
    newl.sort()
    print(newl)
        

  
    # for stuff in data:
    #     print(stuff['total_sales'])
        
