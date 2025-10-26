# Programa para saber si un año es bisiesto


year_ = int(input("Introduce un año: "))

# Aplicar la regla para determinar si es bisiesto

if (year_ % 4 == 0 and year_ % 100 != 0) or (year_ % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año NO es bisiesto.")

