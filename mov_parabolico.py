"""Programa que calcula las coordenadas x e y de un proyectil lanzado con una velocidad vo (m/s)
    y un angulo de inclinacion alp dado en radianes; el proyectil describe un movimiento
    parabolico, se asume que el origen de coordenadas es el punto de lanzamiento y la gravedad es
    9.81 m/s2"""

from math import sin, cos

def pos_parab(vo, alp):
    g = 9.81
    t = float(input("ingrese tiempo en s: ")) 
    tsub = vo * sin(alp)/g
    ttot = 2 * tsub
    hmax = ((vo*sin(alp))**2)/(2*g) 
    if 0<t<tsub:
        x= vo * cos(alp)*t
        y = vo * sin(alp)*t - g * t*t /2
        print(x, y)
    elif tsub <t<ttot:
        x = vo * cos(alp)*t
        y = hmax - (g * (t - tsub)**2)/2
        print(x, y)
    
    else:
        print('datos incorrectos')
 

"""hallamos la posicion del proyectil con una velocidad inicial de 5 m/s y un angulo
     de inclinacion de 0.523 rad ≊ 29.97°"""        

pos_parab(5, 0.523)   