"""Define tres listas de 20 números enteros cada uno,
con nombres number, square y cube. Carga las lista number
con valores aleatorios entre 0 y 100. En la lista square se deben
almacenar los cuadrados de los valores que hay en number.
En la lista cube se deben almacenar los cubos de los valores que hay en number.
A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.
Francisco José García Jurado"""

import numpy as np


number = np.random.randint(0, 101, size=20)

square = number ** 2

cube = number ** 3

print(f"{'Number':>10} {'Square':>10} {'Cube':>10}")
for x in range(20):
    print(f"{number[x]:>10} {square[x]:>10} {cube[x]:>10}")



