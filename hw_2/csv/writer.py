import csv
 

data = [
    ['os_prod_list', 'os_name_list', 'os_code_list', 'os_type_list'],
    ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],
]

dict_data = [{
    'os_prod_list': 'Изготовитель системы',
    'os_name_list': 'Название ОС',
    'os_code_list': 'Код продукта',
    'os_type_list': 'Тип системы'
}
]

with open('csv/data.csv', 'w') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
with open('csv/dict_data.csv', 'w') as file:
    writer = csv.DictWriter(
        file, 
        fieldnames=['os_prod_list', 'os_name_list', 'os_code_list', 'os_type_list'],
    )
    writer.writeheader()
    for itm in dict_data:
        writer.writerow(itm)