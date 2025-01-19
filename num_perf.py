# programa que calcula los números perfectos que hay entre 1 y 10000
# número perfecto es aquel número que es igual a la suma de sus divisores sin incluir el número
# ej: número = 15 -> divisores: 1, 3, 5  1+3+5 = 9 != 15  -> 15 no es número perfecto
#     número = 28 -> divisores: 1, 2, 4, 7, 14   1+2+4+7+14 = 28 = 28 -> 28 es número perfecto 

def divisores(num):
    lista = []
    for i in range(1, num):  # itera desde 1 hasta num-1 para que nos dé todos los divisores menos el mismo número
        if num % i == 0:
            lista.append(i)
    return lista

def es_numero_perfecto(num):
    if sum(divisores(num)) == num:
        return num
    
for i in range(1, 10000):
    if es_numero_perfecto(i):
        print(i)