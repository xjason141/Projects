import os
import requests

for files in os.listdir('data/feedback/'):
    n_keys = ['title', 'name', 'date', 'feedback']
    count = 0
    n_dict = {}
    with open('data/feedback/' + files, 'r') as file:
        for lines in file:
            n_dict[n_keys[count]] = lines.rstrip()
            count += 1
    # print(n_dict)
    response = requests.post('http://<corpweb-external-IP>/feedback', json=n_dict)
print(response.status_code)