#Implementación de escritura en archivos csv
import csv

#Definir nombre de un archivo
filename = 'tmp/archivo_fake.csv'
columns = ['id','name','age']

with open(filename, mode='w', newline= '') as csv_file: #w = writer
    writer = csv.DictWriter(csv_file, fieldnames=columns) #escribre un archivo csv con este nombre de columnas


    writer.writeheader() #escriba primera fila con los encabezados de las columnas

    counter = 1
    while counter <= 20:
        writer.writerow({
            'id': counter * 123,
            'name':f'Dalai {counter}{counter * 234}',
            'age': f'{counter * 5}'
        })
        counter += 1