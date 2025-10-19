# Juego del dado
# Crea un programa que simule el lanzamiento de dos dados.
# El programa preguntará cuántas tiradas quiere realizar el usuario.
# Después de realizar todas las tiradas, debe mostrar:

# Cuántas veces ha salido doble (los dos dados con el mismo número).
# Cuántas veces la suma de los dados ha sido 7.
# La suma total de todos los valores obtenidos.
# Usa el módulo random para generar números del 1 al 6.
# Autor: Francisco José García Jurado
import random as rd
count_equals = 0
count_seven = 0
total_sum = 0

tiradas = int(input("Ingrese la cantidad de tiradas: "))

for i in range(tiradas):
    dado1 = rd.randint(1, 6)
    dado2 = rd.randint(1, 6)
    print ("Dado 1: ", dado1, "Dado 2: ", dado2)
    total_sum += dado1 + dado2
    if dado1 == dado2:
        count_equals += 1
    elif dado1 + dado2 == 7: #Solo comparo si suman 7 si son distintos los dados
        count_seven += 1

print(f"El total de las tiradas es: {total_sum}")
print(f"El total de dobles es: {count_equals}")
print(f"El total de sietes es: {count_seven}")





