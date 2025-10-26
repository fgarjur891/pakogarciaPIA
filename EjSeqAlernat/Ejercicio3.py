# 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

print ("Calcularemos la hipotenusa de un triángulo")
cateto1 = float(input('Cateto1: '))
cateto2 = float(input('Cateto2: '))

hipo = float((cateto1**2 + cateto2**2)**0.5)

print ('La hipotenusa es ',hipo)
