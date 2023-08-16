# prog que suma los precios de los articulos con sus impuestos incluidos y calcula el impuesto
# total a pagar 
def preciofinal(imp, *articulos):
    total = 0
    for articulo in articulos:
        total += articulo
        
    print("El total a pagar es {0}".format(total))
    print("El impuesto es {0:.2f}% y el impuesto a pagar es {1}".format(imp, (imp/100)*total))
    
"""
    p.e tenemos los siguientes articulos con sus respectivos precios y sus impuestos incluidos
    
    azucar = 100            imp = 15 %
    arroz = 250
    aceite = 150
    pollo = 400
"""

preciofinal(15, 100, 250, 150, 400)