import math

# funcion que calcula las raices de una ecuacion de 2do grado (ax**2 + bx + c = 0)
def ecuacion_2():
    
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    c = int(input("Ingrese el valor de c: "))
    disc = b ** 2 - 4 * a * c  # discriminante de la ecuacion de 2do grado
    
    if (disc == 0):
        print(f"La ecuacion tiene una unica raiz de multiplicidad 2 y es {-b/(2*a)}")
        
    elif (disc > 0):
        print("La ecuacion tiene dos raices reales")
        print(f"La primera raiz es {(-b + math.sqrt(disc))/(2 * a)}")
        print(f"La segunda raiz es {(-b - math.sqrt(disc))/(2 * a)}")
        
    else:
        print("Las raices son complejas conjugadas")
        print(f"La primera raiz es {-b/(2*a)} + {(math.sqrt(-disc))/(2 * a)}i ")
        print(f"La segunda raiz es {-b/(2*a)} - {(math.sqrt(-disc))/(2 * a)}i ")
        
# llamada a la funcion
ecuacion_2()        