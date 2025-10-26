# Programa para calcular el costo de una llamada telefónica

# Leer datos de entrada
# Duración de la llamada en minutos (puede ser decimal)
minutos = float(input("Introduce la duración de la llamada en minutos: "))

# Día: "domingo" o "otro" (puedes escribir domingo u otro texto)
dia = input("Introduce el día (escribe 'domingo' si es domingo, cualquier otra cosa si no): ")

# Turno: "mañana" o "tarde" (solo se usa si NO es domingo)
turno = ""
if dia.lower() != "domingo":
    turno = input("Introduce el turno ('mañana' o 'tarde'): ")

# Calcular el costo bruto por tramos
# Tramos:
# - Primeros 5 min: 1.00 €/min
# - Siguientes 3 min (del 6 al 8): 0.80 €/min
# - Siguientes 2 min (del 9 al 10): 0.70 €/min
# - A partir del minuto 10 en adelante (minuto 11 en adelante): 0.50 €/min

# Creamos una variable auxiliar "restante" para ir descontando los minutos
# que vamos asignando a cada tramo, sin modificar la variable original "minutos"
restante = minutos


# Tramo 1: hasta 5 minutos a 1.00 €/min
# Si quedan menos de 5 minutos, usamos todos; si no, usamos solo 5
if restante < 5:
    t1 = restante
else:
    t1 = 5

costo_tramo1 = t1 * 1.00
restante = restante - t1

# Tramo 2: siguientes 3 minutos (del minuto 6 al 8) a 0.80 €/min
if restante > 0:
    # Si quedan menos de 3 minutos, usamos todos; si no, usamos solo 3
    if restante < 3:
        t2 = restante
    else:
        t2 = 3
    
    costo_tramo2 = t2 * 0.80
    restante = restante - t2

# Tramo 3: siguientes 2 minutos (del minuto 9 al 10) a 0.70 €/min
if restante > 0:
    # Si quedan menos de 2 minutos, usamos todos; si no, usamos solo 2
    if restante < 2:
        t3 = restante
    else:
        t3 = 2
    
    costo_tramo3 = t3 * 0.70
    restante = restante - t3

# Tramo 4: resto a partir del minuto 11 a 0.50 €/min
if restante > 0:
    t4 = restante
    costo_tramo4 = t4 * 0.50
    restante = 0

# Sumar costos de todos los tramos para obtener el costo bruto (sin impuesto)
costo_bruto = costo_tramo1 + costo_tramo2 + costo_tramo3 + costo_tramo4

# 3) Calcular impuesto según día/turno
# - Si es domingo: 3%
# - Si no es domingo y turno mañana: 15%
# - Si no es domingo y turno tarde: 10%
if dia.lower() == "domingo":
    porcentaje_impuesto = 0.03
else:
    if turno.lower() == "mañana":
        porcentaje_impuesto = 0.15
    else:
        porcentaje_impuesto = 0.10

# Calcular el importe del impuesto y el total a pagar
impuesto = costo_bruto * porcentaje_impuesto
total_a_pagar = costo_bruto + impuesto

# 4) Mostrar desglose de costos
print("")
print("Minutos hablados:", minutos)
print("Costo tramo 1 (0-5 min a 1.00 €/min):", round(costo_tramo1, 2), "€")
print("Costo tramo 2 (6-8 min a 0.80 €/min):", round(costo_tramo2, 2), "€")
print("Costo tramo 3 (9-10 min a 0.70 €/min):", round(costo_tramo3, 2), "€")
print("Costo tramo 4 (desde min 11 a 0.50 €/min):", round(costo_tramo4, 2), "€")
print("Costo bruto (sin impuesto):", round(costo_bruto, 2), "€")

# Mostrar cuál impuesto aplicó según el día y turno
if dia.lower() == "domingo":
    print("Impuesto aplicado: 3% (domingo)")
else:
    if turno.lower() == "mañana":
        print("Impuesto aplicado: 15% (turno de mañana)")
    else:
        print("Impuesto aplicado: 10% (turno de tarde)")

print("Importe del impuesto:", round(impuesto, 2), "€")
print("Total a pagar:", round(total_a_pagar, 2), "€")