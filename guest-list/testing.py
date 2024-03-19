import json

newdict = {'name': 'didi', 'age': 45}
prep = {'random':[newdict]}


# with open('guest-list/testing.json', 'w') as f:
#     json.dump(prep, f, indent=2)

with open('guest-list/testing.json') as f:
    data = json.load(f)
    for things in data['random']:
        print(things)
        