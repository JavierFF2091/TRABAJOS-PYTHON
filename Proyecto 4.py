from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Hola, ¿Me puedes decir tu nombre?: ")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100.\nTienes solo ocho intentos para adivinar cuál crees que es el número.")

while intentos <8:
    estimado = int(input("¿Cuál es el número?: "))
    intentos += 1

    if estimado not in range (1, 101):
        print("Tu numero no se en encuentra en el rango que va de 1 a 100")
    elif estimado < numero_secreto:
        print("Mi numero es mas alto")
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    else:
        print(f"¡Felicidades {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento {nombre}, se han agotado los intentos. El número secreto era {numero_secreto}")




