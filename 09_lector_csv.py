#Utilizado modulo CSV para lectura de archivos csv

import csv

filename = 'employees.csv'

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file) #para que lea el archivo
    for row in csv_reader:   
        print(row)