#!/usr/bin/python3

class Vehicle:
    #fixed attribute
    color = 'white'

    def __init__(self, name:str, max_speed:int, mileage:int):        
        #instance attributes
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seat_capacity(self, capacity:int):
        return f'The seating capacity of a {self.name} is {capacity} passengers'

class Bus(Vehicle):
    pass


class Car(Vehicle):
    def seat_capacity(self, capacity: int = 6):
        return super().seat_capacity(capacity)



x = Car('merc',250, 25)

print(f'Name: {x.name} with max speed of {x.max_speed}km/h, using only {x.mileage}l/km. {x.seat_capacity(4)}')
