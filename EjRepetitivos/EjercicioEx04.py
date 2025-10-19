# Crea un programa que pida al usuario un número entero positivo N
# y muestre un triángulo numérico creciente.
# Autor: Francisco José García Jurado

number = int(input("Dame el número para hacer tu triángulo: "))
while number <= 0:
    number = int(input("El número debe ser mayor que 0: "))
count = 1
for j in range(1, number + 1):
    for i in range(1, count+1):
        print (f"{i:3} ",end=" ")
    count += 1
    print()





