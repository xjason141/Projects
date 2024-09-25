y = 'hee'
try:
    int(y)
except ValueError as err:
    print(type(err).__name__ + ': Invalid ID. ID should only be numbers.')