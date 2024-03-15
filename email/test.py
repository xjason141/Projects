import cars
import locale
import json


"""Loads the contents of filename as a JSON file."""
with open('email/car_sales.json') as things:
    item_sales = things['total_sales']
    print(item_sales)

    