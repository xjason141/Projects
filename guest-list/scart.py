import os

exist = os.path.exists('C:\Users\US\Py\Projects\guest-list')

pathing = os.path.dirname(os.path.realpath(__file__))

print(exist)