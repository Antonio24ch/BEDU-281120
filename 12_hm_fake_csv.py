# Implementacion de escritura en archivos csv
import csv

filename = 'tmp/archivo_fake.csv'
columns = ['id', 'name', 'age']

def fake_id():
    pass

def fake_name():
    pass

def fake_age():
    pass

with open(filename, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=columns)

    writer.writeheader()

    counter = 1
    while counter <= 20:
        writer.writerow({
            'id': fake_id(),
            'name': fake_name(),
            'age': fake_age()
        })
        counter += 1