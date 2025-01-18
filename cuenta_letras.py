def cuenta_letras(text):
    count = 0
    palabras = text.split()
    for palabra in palabras:
        for letra in palabra:
            if letra.isalpha():
                count += 1
    return count


print(cuenta_letras("vamos a la playa todos a gozar"))
