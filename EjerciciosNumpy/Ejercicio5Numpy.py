"""Escribe un programa que genere 20 números enteros entre 100 y 999.
Estos números se deben introducir en una lista de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas
igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.
Francisco José García Jurado"""

import numpy as np

# Generar 20 números enteros aleatorios entre 100 y 999
numbers = np.random.randint(100, 1000, size=20)

# Reshape para crear una matriz de 4 filas y 5 columnas
matrix = numbers.reshape(4, 5)

# Calcular sumas parciales de filas y columnas
row_sums = matrix.sum(axis=1)
col_sums = matrix.sum(axis=0)
total_sum = matrix.sum()

# Mostrar la matriz con sumas parciales
print("Matriz con sumas parciales:")
for i in range(4):
    for j in range(5):
        print(f"{matrix[i, j]:>6}", end="")
    print(f" {row_sums[i]:>6}")  # Suma de la fila

for j in range(5):
    print(f"{col_sums[j]:>6}", end="")
    
print(f" {total_sum:>6}")  # Suma total

