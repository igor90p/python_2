import json


data = {
    'item': 'shoes',
    'quantity': 3, 
    'price': 100, 
    'buyer': 'Ivan', 
    'date': '06/03/2019'
}



with open ('json/orders.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('json/orders.json') as file:
    print(json.load(file))
