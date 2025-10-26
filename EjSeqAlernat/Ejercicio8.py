# 8. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de los siguientes porcentajes:
#* 55% del promedio de sus tres calificaciones parciales.
#* 30% de la calificación del examen final.
#* 15% de la calificación de un trabajo final.

print("Calculamos tu nota final")

parcial1 = float(input("Parcial 1: "))
parcial2 = float(input("Parcial 2: "))
parcial3 = float(input("Parcial 3: "))

average = (parcial1 + parcial2 + parcial3) / 3
final = float(input("Examen final: "))
work = float(input("Trabajo: "   ))
points = average * 0.55 + final * 0.3 + work * 0.15

print ("Su calificación final es: ", points)
