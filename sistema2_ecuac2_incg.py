"""
  Sea un sistema de 2 ecuaciones con 2 incognitas:
  ax + by = c  y  dx + ey = f, hay tres posibles casos para este sistema de ecuaciones
  1) El sistema tenga infinitas soluciones: si se cumple que: a*e = b*d y ademas e*c = f*b
  2) El sistema no tiene solucion: si se cumple que: a*e = b*d pero e*c != f*b
  3) El sistema tiene un conjunto solucion, osea un unico valor para la variable 'x' y
       un unico valor para la variable 'y'; tal que x = (f*b - e*c)/(d*b - a*e)
       e  y = (a*f - c*d)/(e*a - d*b)     
"""

a = int(input("ingrese el valor de a: "  ))
b = int(input("ingrese el valor de b: "  ))
c = int(input("ingrese el valor de c: "  ))
d = int(input("ingrese el valor de d: "  ))
e = int(input("ingrese el valor de e: "  ))
f = int(input("ingrese el valor de f: "  ))

if(a*e == b*d):
    if(e*c == f*b):
        print("El sistema presenta infinitas soluciones")
        
    else:
        print("El sistema no tiene solucion; llamado tambien sistema incompatible")
        
else:
    print(f"El valor de x es {((f*b - e*c)/(d*b - a*e)):.3f} y el valor de y es {((a*f - c*d)/(e*a - d*b)):.3f}")