import cars
import locale
import json
from operator import attrgetter

#get the year with the most total_sales


"""Loads the contents of filename as a JSON file."""
with open('email/car_sales.json') as f:
    data = json.load(f)
    sales_by_year = {}
    for item in data:
        item_year = item["car"]["car_year"]
        sales_by_year[item_year] = sales_by_year.setdefault(item_year, 0) + item['total_sales']
    
    most_popular_year = sorted(sales_by_year, key=sales_by_year.get, reverse=True)[0]
    most_popular_sales = sales_by_year[item_year]
    print(most_popular_year)
    print(most_popular_sales)

# newd = {'stud':{
#     'name': 'didi',
#     'score': 10
# },
# 'stud':{
#     'name': 'dodo',
#     'score': 50
# },
# 'stud': {
#     'name': 'didi',
#     'score': 30
# },
# 'stud': 'dodo',
# 'score': 20
# } 
# #didi=40, dodo=70

# values = newd['stud']
# print(sales_by_year)

