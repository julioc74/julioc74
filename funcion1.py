def sumar_lista(*args):
    total = 0
    for arg in args:
        total += arg
    print (f"la suma de los elementos es: {total}" )
    
sumar_lista(3,5,1,9)
sumar_lista(2,-7,4)