#prog que usa *args y argumento por defecto
def preciofinal1(*articulos, imp=15):
    total = 0
    for articulo in articulos:
        total += articulo
    print("El total a pagar es {0}".format(total))
    print("La tasa de impuesto es {0:.1f}% y el impuesto a pagar es {1}".format(imp,(imp/100)*total))
 
""" En esta llamada a la funcion se usa un iterable (tupla) que va a empaquetar los valores 
 dados como parametros y al no escribirse el valor de la tasa de impuesto se sobreentiende
 que es imp = 15"""    
preciofinal1(100, 250, 150, 400)

"""se usa una tupla para empaquetar los valores dados como parametros, pero ademas el valor por 
 defecto de la tasa de impuesto cambia a imp = 20"""
preciofinal1(100, 250, 150, 400, imp=20)