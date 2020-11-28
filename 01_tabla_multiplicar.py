#Preguntar el numero que el usuario quiere multiplicar
numero = int(input('Que número quieres multiplicar?\t'))

print(f'A continuacion se muestra la tabla del {numero}')
print('------------------------------------------------')

#Esta función hace esto:
# n * 1 = n
# n * 2 = n
# n * 3 = n
# ...
for n in range(10):
    indice = n + 1 #Sirve para que si queremos multiplicar cada 2, 3, etc. solo se cambie el numero(1)
    r = numero * indice
    print(f'{numero} * {indice} = {r}')