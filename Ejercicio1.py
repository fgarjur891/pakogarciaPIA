# Ejercicio 1

# Programa que imprima todos los números pares entre dos números
# que se le pidan al usuario.
# Autor: Francisco José García Jurado

number1 = input("Introduce un numero: ")
number2 = input("Introduce otro numero: ")

for number in range(int(number1), int(number2)+1):
    if number % 2 == 0:
        print(number)

