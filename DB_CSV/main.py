import csv

all_data = []
filename = r'north_data/employees_data.csv'
with open(filename, encoding='utf-8') as file:
    data_full = csv.DictReader(file)
    for data in data_full:
        all_data.append(data)

print(all_data)
