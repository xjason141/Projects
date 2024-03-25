import cars
import locale
import json
from operator import attrgetter

#get the year with the most total_sales


"""Loads the contents of filename as a JSON file."""
# with open('email/car_sales.json') as f:
#     data = json.load(f)
#     sales_by_year = {}
#     for item in data:
#         item_year = item["car"]["car_year"]
#         sales_by_year[item_year] = sales_by_year.setdefault(item_year, 0) + item['total_sales']
    
#     most_popular_year = sorted(sales_by_year, key=sales_by_year.get, reverse=True)[0]
#     most_popular_sales = sales_by_year[item_year]
#     print(most_popular_year)
#     print(most_popular_sales)

#explanation for syntax above
# 1. 'item_year' is used to store the car years.
# 2. line 15: iterates over the total_sales of each year. setdefault() is so that each similar year has one placeholder. e.g For each similar year, their total_sales are added up.
# 3. havent fully understood the sorted part




new_dict = [
    {'name': 'didi',
     'score': 50,},
    {'name': 'koko',
     'score': 40},
    {'name': 'didi',
     'score': 20},
    {'name': 'koko',
     'score': 40}
]

arranged =  {}
for students in new_dict:
    names = students['name']
    arranged[names] = arranged.setdefault(names, 0) + students['score']

has_sorted = sorted(arranged, key=arranged.get, reverse=True)[0]
score_sorted = arranged[names]
print(has_sorted)
print(score_sorted)