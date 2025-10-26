# Programa para calcular el desglose mínimo en billetes y monedas de euros

# Leer la cantidad de euros (entero, sin céntimos)
cantidad = int(input("Introduce la cantidad de euros: "))

# Billetes de 500€
billetes_500 = cantidad // 500

# Cantidad se irá actualizando, con el resto de cada billete
cantidad = cantidad % 500
if billetes_500 > 0:
    print(billetes_500, "billete(s) de 500€")

# Billetes de 200€
billetes_200 = cantidad // 200
cantidad = cantidad % 200
if billetes_200 > 0:
    print(billetes_200, "billete(s) de 200€")

# Billetes de 100€
billetes_100 = cantidad // 100
cantidad = cantidad % 100
if billetes_100 > 0:
    print(billetes_100, "billete(s) de 100€")

# Billetes de 50€
billetes_50 = cantidad // 50
cantidad = cantidad % 50
if billetes_50 > 0:
    print(billetes_50, "billete(s) de 50€")

# Billetes de 20€
billetes_20 = cantidad // 20
cantidad = cantidad % 20
if billetes_20 > 0:
    print(billetes_20, "billete(s) de 20€")

# Billetes de 10€
billetes_10 = cantidad // 10
cantidad = cantidad % 10
if billetes_10 > 0:
    print(billetes_10, "billete(s) de 10€")

# Billetes de 5€
billetes_5 = cantidad // 5
cantidad = cantidad % 5
if billetes_5 > 0:
    print(billetes_5, "billete(s) de 5€")

# Monedas de 2€
monedas_2 = cantidad // 2
cantidad = cantidad % 2
if monedas_2 > 0:
    print(monedas_2, "moneda(s) de 2€")

# Monedas de 1€
monedas_1 = cantidad
if monedas_1 > 0:
    print(monedas_1, "moneda(s) de 1€")