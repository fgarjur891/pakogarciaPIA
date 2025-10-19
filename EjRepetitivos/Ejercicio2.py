# Ejercicio 2
# Realizar un algoritmo que pida números (se pedirá por teclado
# la cantidad de números a introducir). El programa debe informar de
# cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
# Autor: Francisco José García Jurado

contador0 = 0
contadorpos = 0
contadorneg = 0

numbers = int(input("Introduce cuantos numeros vas a introducir: "))

for index in range(numbers):
    num = int(input(f"Introduce el numero {index+1}: "))
    if num == 0:
        contador0 += 1
    elif num > 0:
        contadorpos += 1
    else:
        contadorneg += 1

print(f"Número de ceros {contador0} Número de positivos {contadorpos} Número de negativos {contadorneg}")



