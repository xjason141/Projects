import cars
import locale


def calc():
    max_revenue = {"revenue": 0}
    x = cars.load_data('email/car_sales.json')
    for vehicles in x:
        for y in vehicles:
            print(type(y))

calc()

    