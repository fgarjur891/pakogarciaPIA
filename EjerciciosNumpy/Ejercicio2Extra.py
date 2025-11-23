"""
El Ejercicio: "El Alumno Digital"
Vamos a crear una clase llamada Alumno.
Debe tener un método constructor (__init__) que reciba dos cosas:
el nombre del alumno y una lista de notas.

El truco: Dentro del constructor, debes convertir esa lista de notas
en un array de Numpy y guardarlo en un atributo self.notas.

Después, crea un método llamado calcular_promedio que use
Numpy para devolver la media de esas notas.
Francisco José García Jurado
"""

import numpy as np

class Alumno:

    def __init__(self, nombre, lista_notas):
        self.nombre = nombre
        self.notas = np.array(lista_notas)

    def calcular_promedio(self):
        return np.mean(self.notas)

def main():

    # Crear un alumno con una lista de notas
    alumn1 = Alumno("Juan Pérez", [85, 90, 78,])
    alumn2 = Alumno("María Gómez", [23, 33, 55])

    # Calcular y mostrar el promedio de notas
    print(f"El promedio de {alumn1.nombre} es:, {alumn1.calcular_promedio():.2f}")
    print(f"El promedio de {alumn2.nombre} es:, {alumn2.calcular_promedio():.2f}")

main()


