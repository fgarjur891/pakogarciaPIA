# 14. Escribir un programa para calcular la nota final de un examen, considerando que:

# cada respuesta correcta suma 5 puntos
# cada respuesta incorrecta suma -1 puntos
# cada respuesta en blanco suma 0 puntos. 
# Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
# ¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes 
# tipos de respuestas puedan cambiar en el futuro?

# Pienso que se podría realizar preguntando los valores de dicho datos. 

rc = int(input("Respuestas correctas:"))
ri = int(input("Respuestas incorrectas: "))
rb = int(input("Respuestas en blanco:" ))
# calculamos nota final según indicaciones
nota_final = rc * 5 + ri * -1
print("Tu notal final es: ",nota_final)

#normalización sobre 10 con 2 decimales
print ("Nota sobre 10: ",round(10/(rc+ri+rb)*rc,2))
