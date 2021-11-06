# import os
# # os.remove('base.txt')
#

import json

data = {
    'name': 'Tom',
    'surname': 'Cruse',
    'age': 57,
    'cars': ['ferrari, zaz'],
}

#
# with open("data.json", 'w') as f:
#     json.dump(data, f)

with open("data.json", 'r') as f:
    data = json.load(f)

print(data['cars'])