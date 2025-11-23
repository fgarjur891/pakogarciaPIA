"""Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100
y que los almacene en un array de numpy.
El programa debe ser capaz de pasar todos los números pares a las primeras
posiciones del array (del 0 en adelante) y
todos los números impares a las celdas restantes.
Utiliza arrays auxiliares si es necesario."""

import numpy as np

# Generar 20 números enteros aleatorios entre 0 y 100
numbers = np.random.randint(0, 101, size=20)

# Crear arrays para pares e impares
evens = numbers[numbers % 2 == 0]
odds = numbers[numbers % 2 != 0]

# Combinar los arrays de pares e impares
sorted_numbers = np.concatenate((evens, odds))
print("Números originales:", numbers)
print("Números con pares primero:", sorted_numbers)

