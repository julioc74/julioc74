def temp():
    temperatura = input("desea convertir la temperatura de fahrenheit a celsius 'ftoc' o de celsius a fahrenheit 'ctof' ")
    match temperatura:
        # convierte temperatura de fahrenheit a celsius
        case 'ftoc': 
            t = float(input("ingrese temp en fahrenheit "))
            c = (t - 32) * 5 / 9
            print(f"La temperatura en celsius es {c:.2f} celsius")
        # convierte temperatura de celsius a fahrenheit
        case 'ctof':
            t = float(input("ingrese tempft en celsius "))
            f = t * 9 / 5 + 32
            print(f"la temperatura en fahrenheit es {f:.2f} fahrenheit")
        # cuando se ingresa una distinta a las anteriores
        case _:
            print("Ingrese temperatura en celsius o fahrenheit solamente")
            
temp()