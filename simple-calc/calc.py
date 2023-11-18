#!/usr/bin/python3

import sys

print('WELCOME TO THIS EXREMELY SIMPLE CALCULATOR')

print('''Select an operation
      1. Addition
      2. Substraction
      3. Multiplication
      4. Division''')

select = int(input('Please enter the operation\'s number '))

if select in range(5):
    pass
else:
    sys.exit('Please select a number between 1 - 4')
    
num1 = input('Enter a number: ')
num2 = input('Enter a number: ')

def calc():
    if select == 1:
        res = int(num1) + int(num2)
        return res
    if select == 2:
        res = int(num1) - int(num2)
        return res
    if select == 3:
        res = int(num1) * int(num2)
        return res
    if select == 4:
        res = int(num1) / int(num2)
        return res
    
print('Your result is ' + str(calc()))

print('testing here')