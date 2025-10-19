# Cuadro numérico progresivo
# Crea un programa que pida al usuario un número entero N
# y muestre en pantalla un cuadro numérico de tamaño N x N
# Autor: Francisco José García Jurado
number = int(input("Introduce el número N:"))
while number <= 0:
    number = int(input("El número tiene que ser mayor que 0: "))
count = 1

for i in range(number):
    for j in range(number):
        print(f"{count:3}", end=" ")
        if (count)  % number == 0:
            print (" ")
        count += 1