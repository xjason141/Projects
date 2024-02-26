import os
import requests


for files in os.listdir('data/feedback/'):
    n_keys = ['title', 'name', 'date', 'feedback']
    n_dict = {}
    count = 0
    with open('data/feedback/' + files, 'r') as file:
        for lines in file:
            n_dict[n_keys[count]] = lines.rstrip()
            count += 1
    print(n_dict)
    


# print(str(count) + ' lines in total')













