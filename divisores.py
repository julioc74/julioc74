def divisores(num):
    lista = []
    for i in range(1, num+1):
        if num % i == 0:
            lista.append(i)
    print(f"La lista de divisores de {num} es {lista}")
    

    