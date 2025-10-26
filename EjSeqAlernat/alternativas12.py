# Programa que pide cinco números enteros y muestra el mayor (usando sorted)

# Leer los cinco números y guardarlos en una lista
n1 = int(input("Introduce el número 1: "))
n2 = int(input("Introduce el número 2: "))
n3 = int(input("Introduce el número 3: "))
n4 = int(input("Introduce el número 4: "))
n5 = int(input("Introduce el número 5: "))

# Crear una lista con los cinco números
numeros = [n1, n2, n3, n4, n5]

# Ordenar la lista de menor a mayor (he cogido la idea del video)
numeros_ordenados = sorted(numeros)

# El último elemento de la lista ordenada es el mayor
mayor = numeros_ordenados[4]  # índice 4 es la quinta posición (0, 1, 2, 3, 4)

print("El mayor es:", mayor)