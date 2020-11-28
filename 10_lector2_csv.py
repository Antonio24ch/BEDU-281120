
import csv

filename = 'employees.csv'

with open(filename, mode='r') as csv_file: #modo r = read
    csv_reader = csv.DictReader(csv_file) #la funcion DictReader es de mode='r'
    for row in csv_reader:   
        #print(row['Salary']) #para acceder algun dato pero es más recomendable ejecutarlo como se muestra abajo:
        #print(row.get('Salary')) #para imprimir una sola variable
        s = row.get('Salary')
        n = row.get('Name')
        print(f'{n}: earns ${s}') #dos variables