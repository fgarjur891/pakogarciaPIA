# Ejercicio 7

# Crea un programa que nos permita calcular la cuota de una hipoteca
# y su tabla de amortización después de que se pida al usuario/a:
# Importe del préstamo. La tasa de interés anual. Y el plazo de pago en años.
# Autor: Francisco José García Jurado

cantidad = 0
tasa = 0
years = 0

#Validación datos entrada solo dígitos y con punto decimal
while True:
    cantidad = input("Cantidad del préstamo: ")
    if  cantidad.replace('.', '', 1).isdigit():
        if float(cantidad) > 0:
            cantidad = float(cantidad)
            break
        else:
            print("Solo cantidades positivas")
    else:
        print("Utilice solo . decimal")

while True:
    tasa = input("Cantidad de la tasa de interes: ")
    if tasa.replace('.', '', 1).isdigit():
        if float(tasa) > 0:
            tasa = float(tasa)
            break
        else:
            print("Solo cantidades positivas")
    else:
        print("Utilice solo . decimal")


while True:
    years = input("Número de años: ")
    if years.isdigit():
        if int(years) > 0:
            years = int(years)
            break
        else:
            print("Cantidades solo mayores que 0")
    else:
        print("Utilice solo digitos decimal")

num_meses = years * 12
tasa_mes =  (float(tasa) / 100) / 12

cuota = cantidad * (tasa_mes * (1 + tasa_mes) ** num_meses) / ((1 + tasa_mes ) ** (num_meses) - 1)
restante = cantidad

print(f"Cuota cada mes: {cuota:.2f} €")

print("\n Plan de amortización \n")
for i in range(1, num_meses + 1):
    interes_cuota = restante * tasa_mes
    capital_cuota = cuota - interes_cuota
    print(f"Mes: {i} {cuota:.2f} Resta: {restante:.2f}")
    print(f"De interes {interes_cuota:.2f} Capital: {capital_cuota:.2f}\n")
    restante = restante - capital_cuota



