import os

def calc(x):
    z = x + 10
    print(z)

def mid(x):
    z = x * 10
    print(z)

exist = os.path.isfile('place.csv')

if exist == False:
    calc(5) #answer is 15
else:
    mid(5)#answer is 50