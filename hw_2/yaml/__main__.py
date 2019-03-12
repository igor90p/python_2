import yaml


data_cost = ['300€', '500€', '800€',]

data = {
    'name': 'suit',
    'count': 3,
    'cost': data_cost
}

with open('yaml/conf.yml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode = True)

with open('yaml/conf.yml') as file:
    print(yaml.load(file))