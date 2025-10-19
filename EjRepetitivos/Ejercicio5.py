#Ejercicio 5
# Crea un programa que pida un número por teclado al usuario y
# diga si es primo. En caso de que no se introduzca un número
# o que esta sea menor que 2 se debe mostrar un mensaje de error.
# Autor: Francisco José García Jurado
divisors = 1
number = input("Dime un número mayor o igual a 2: ")

if number.isdigit():
    number = int(number)
    if number >= 2:
        for i in range(1, (number // 2) + 1):
            if number % i == 0:
                divisors += 1

        if divisors == 2 :
            print ("El número es primo")
        else:
            print ("No es primo")
    else:
        print("Has introducido un número menor de 2")
else:
    print ("Eso es una letra")
