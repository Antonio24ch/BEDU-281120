#Aplicar conocimientos de la función MAP en python

#PUNTOS A REALIZAR:
#Agregar descuento aleatorio entre 5, 10 y 15 % a los precios 
#Imprimir menu sin descuento
#Imprimir menu con descuento
import random

precios_en_menu = [60,87,45,66,25,33,55,88,100]

descuento = [0.05,0.10,0.15]

#por_de_descuento = random.sample(descuento, k = 1)
#print(porcentaje_con_descuento)
porcentaje_descuento = random.choice(descuento)
input(f'Tu descuento es de {porcentaje_descuento}')

def descuento(precios):
    result = (precios * porcentaje_descuento)
    result1 = precios - result
    return round(result1,2)

print(precios_en_menu)

# Usar map para aplicar una función a cada elemento de mi lista
precios_con_desc = list(map(descuento,precios_en_menu))
print(precios_con_desc)






