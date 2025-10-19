#Escribe un programa que pida el limite inferior y superior
# de un intervalo. Si el límite inferior es mayor que el superior
# lo tiene que volver a pedir.

#A continuación se van introduciendo números hasta que introduzcamos el 0.
# Cuando termine el programa dará las siguientes informaciones:

#-La suma de los números que están dentro del intervalo (intervalo abierto).
#-Cuantos números están fuera del intervalo.
#-Informa si hemos introducido algún número igual a los límites del intervalo.

while True:
    lower_limit = float(input("Introduce el límite inferior del intervalo: "))
    upper_limit = float(input("Introduce el límite superior del intervalo: "))

    if lower_limit < upper_limit:
        break
    else:
        print("El límite inferior debe ser menor que el superior. \n")

sum_inside = 0
count_outside = 0
equals = False

while True:
    number = float(input("Introduce un número (0 para terminar): "))

    if number == 0:
        break

    if (lower_limit < number) and (number < upper_limit):
        sum_inside += number
    elif number == lower_limit or number == upper_limit:
        equals = True
    else:
        count_outside += 1

print("\n Resultados:")
print(f"Suma de los números dentro del intervalo (abierto): {sum_inside}")
print(f"Números fuera del intervalo: {count_outside}")
if equals:
    print("Se ha introducido al menos un número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")

