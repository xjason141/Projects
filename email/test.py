import cars
import locale
import json

#get the year with the most total_sales


"""Loads the contents of filename as a JSON file."""
with open('email/car_sales.json') as f:
    data = json.load(f)
    sales_by_year = {}
    for item in data:
        item_year = item["car"]["car_year"]
        sales_by_year[item_year] = sales_by_year.setdefault(item_year, 0) + item['total_sales']
    print(sales_by_year)
