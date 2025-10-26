# 7. Realiza un programa que reciba una cantidad de minutos y muestre 
# por pantalla a cuantas horas y minutos corresponde.

minutos = int(input("Minutos: "))
horas = minutos // 60
min_rest = minutos % 60 
print ("Son ",horas, "horas y ", min_rest, "minutos")
