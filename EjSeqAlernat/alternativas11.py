# Programa que pide tres números enteros y muestra el mayor

# Leer los tres números como enteros
a = int(input("Introduce el primer número entero: "))
b = int(input("Introduce el segundo número entero: "))
c = int(input("Introduce el tercer número entero: "))

# Suponemos inicialmente que el mayor es 'a'
mayor = a

# Comparamos con 'b'
if b > mayor:
    mayor = b  # Si b es mayor que el actual 'mayor', actualizamos

# Comparamos con 'c'
if c > mayor:
    mayor = c  # Si c es mayor que el actual 'mayor', actualizamos

print("El mayor es:", mayor)