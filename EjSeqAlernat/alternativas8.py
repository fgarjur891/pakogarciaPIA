# El director de una escuela está organizando un viaje de estudios, 
# y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar 
# a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: 
# si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, 
# el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, 
# el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. 
# Realiza un programa que permita determinar el pago a la compañía de autobuses 
# y lo que debe pagar cada alumno por el viaje.

alumnos = int(input("Indica número de alumnos que viajan: "))

if alumnos < 30:
    print ("El viaje son 4000€ y cada alumno debe pagar", round(4000/alumnos,2),"€")
elif alumnos < 49:
    print ("Cada alumno debe pagar 95€ y el total es: ",alumnos*95)
elif alumnos < 100:
    print ("Cada alumno pagará 70€ y el total es: ", alumnos*70)
else:
    print ("Cada alumno pagará 65€ y el total es: ",alumnos*65)
