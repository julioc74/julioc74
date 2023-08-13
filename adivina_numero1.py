from random import randint

def adivina():
    intentos = 4
    num_pc = randint(1, 15)
    while(intentos >= 0):
        print(f"Tiene {intentos + 1} intentos de adivinar")
        numero = int(input("Ingrese un numero entre 1 y 15:  "))
        
        if (numero != num_pc):
            intentos -= 1
            print("Intente de nuevo")
        else:
            print("Acertastes!, felicidades")
            break
    else:
        print("Lo siento, Fin del juego")

adivina()
        
    