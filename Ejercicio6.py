#Ejercicio 6
#Crea un programa que muestre en pantalla los N primeros número primos.
# El valor de N se pide por teclado al usuario/a.

count_primos = 0

numbers = input("Dime cuántos números primos quieres ver: ")

if numbers.isdigit() and int(numbers) >= 1:
    numbers = int(numbers)
    count = 2  # Empezamos con el primer número primo real

    while count_primos < numbers:
        divisors = 0

        # Contamos cuántos divisores tiene 'count'
        for i in range(1, count + 1):
            if count % i == 0:
                divisors += 1

        # Si tiene exactamente 2 divisores (1 y él mismo) es primo
        if divisors == 2:
            print(count, end=" ")
            count_primos += 1

        count += 1
else:
    print("Datos de inicio incorrectos.")

