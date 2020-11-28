precios_en_menu = [25,87,32,66,25,10,55,88,100]
 
IVA = 0.16

for precio in precios_en_menu:
    result = precio * (1+IVA)
    print(f'${precio} con IVA incluido: $', round(result,2))