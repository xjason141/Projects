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
        
    most_popular_sales = sorted(sales_by_year.items(), key=lambda item: item[1], reverse=True)
    print('the best year is {} with {} sales'.format(most_popular_sales[0][0], most_popular_sales[0][1]))