import random


numero_secreto = random.randint(0,101)
cant_intentos = 0
cant_max_intentos = 10
adivinado = False

print("BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("GAME OVER! NO TIENES MAS INTENTOS")
        break
    
    numero = int(input("INTRODUCE UN NUMERO DEL 1 AL 100: "))

    if numero == numero_secreto:
        print("FELICITACIONES! ADIVINASTE EL NUMERO SECRETO!!")
        adivinado = True

    elif numero < numero_secreto:
        print("EL NUMERO ES MAS ALTO")
    else:
        print("EL NUMERO ES MAS BAJO")

    cant_intentos += 1
              