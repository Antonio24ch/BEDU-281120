# Usando la función MAP en python

precios_sin_iva = [25,87,32,66,25,10,55,88,100]

IVA = 0.16

def aplicar_iva(precio):
    result = precio * (1 + IVA)
    return round(result,2)

print(precios_sin_iva)

# Usar map para aplicar una función a cada elemento de mi lista
precios_con_iva = list(map(aplicar_iva,precios_sin_iva))
print(precios_con_iva)

