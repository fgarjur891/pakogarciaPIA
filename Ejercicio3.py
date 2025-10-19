# Ejercicio 3
# Crea una aplicación que permita adivinar un número. La aplicación
# genera un número aleatorio del 1 al 100. A continuación va pidiendo
# números y va respondiendo si el número a adivinar es mayor o menor que el
# introducido, además de los intentos que te quedan
# (tienes 10 intentos para acertarlo). El programa termina cuando
# se acierta el número (además te dice en cuantos intentos lo has acertado),
# si se llega al limite de intentos te muestra el número que había generado.

import random as rd

oportunities = 0

#Número aleatorio entre 1 y 100
number_rd = rd.randint(1, 100)
print("He pensado un número entre 1 y 100, tienes 10 intentos para adivinarlo")

for oportunities in range(10):
    number = int(input(f"Dime el número {oportunities+1}: "))
    if number == number_rd:
        print(f"Waw¡¡ lo has acertado en {oportunities + 1} intentos ")
        break
    elif number > number_rd:
        print(f"Te quedan {10 - oportunities - 1} intentos")
        print ("Me has dicho un número mayor")
    else:
        print(f"Te quedan {10 - oportunities - 1} intentos")
        print ("Me has dicho un número menor")





