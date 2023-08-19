import math

print("Ingrese los lados del triangulo a construir")
a = int(input("Ingrese el valor de lado a: "))
b = int(input("Ingrese el valor de lado b: "))
c = int(input("Ingrese el valor de lado c: "))

"""Se sabe por teoria de geometria, que para que se de la existencia de un triangulo cada lado de un triangulo 
    debe ser mayor a cero; y ademas cada lado debe ser mayor al valor absoluto de la diferencia de los otros 
    dos lados y a su vez debe ser menor a la suma de los otros dos lados.
    Es decir se deben cumplir todas estas condiciones para que la existencia de dicho triangulo sea verdadera
    de lo contrario; basta que una condicion no se cumpla la existencia de dicho triangulo es falsa."""
def es_triangulo(a, b, c):
    if(a>0 and b>0 and c>0 and 
       abs(b - c) < a < b + c and 
       abs(a - c) < b < a + c and 
       abs(a - b) < c < a + b):
        
        print("El triangulo existe") 
        return True
    
    else:
        print("El triangulo no existe")
        return False
        

# Funcion que calcula el area de un triangulo usando la formula de Heron 
def area_heron(a, b, c):
    if(es_triangulo(a, b, c)):
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("El area del triangulo por la formula de Heron es: {:.3f}".format(area))
        
    else:
        print("Fin del programa")

# llamada a la funcion area_heron(a,b,c)        
area_heron(a, b, c)