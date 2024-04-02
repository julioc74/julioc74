"""Metodo para hallar la altura alcanzada por un proyectil lanzado desde el suelo en direccion 
    perpendicular a la superficie, donde:
    vo es la velocidad inicial del proyectil lanzada desde el suelo hacia arriba de manera perpendicular dado en m/s
    g es la aceleracion de la gravedad dado en m/s2
    tsub es el tiempo de subida del proyectil, osea hasta que logre su altura maxima en s (seg)
    tbaj es el tiempo de bajada del proyectil hasta que impacta nuevamente en el suelo
    hmax es la altura maxima alcanzada por el proyectil dado en m
    h es la altura lograda respecto al nivel del suelo
    Todo esto considerando condiciones ideales (sin rozamiento del aire)"""
def altura(vo):
    g = 9.8
    tsub = vo/g
    tbaj = 2*tsub
    hmax = (vo*vo)/(2*g)
    t = float(input("ingrese el tiempo en seg "))
    if t < tsub:
        h = vo*t - g * t * t/2
        print(f"la altura alcanzada por el proyectil es de {h:.3f}m")
    
    elif tsub < t < tbaj:
        h = ((vo*vo)/(2*g) - g*(t-vo/g)*(t-vo/g)/2)
        print(f"la altura alcanzada por el proyectil es de {h:.3f}m")

# hallando la altura, para una velocidad inicial de 10 m/s con un tiempo t dado por consola 
altura(10)