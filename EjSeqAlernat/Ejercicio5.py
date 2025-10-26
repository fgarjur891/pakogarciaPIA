# 5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

print ("Conversión de F a C")

grados_f = float(input("Indique ºF a convertir: "))
grados_c = (grados_f - 32) * 5 / 9

print("ºC = ",grados_c)
