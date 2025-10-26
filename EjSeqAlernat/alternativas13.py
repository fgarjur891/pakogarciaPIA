# Programa: dado un primer número y otros cuatro, indicar cuál de los cuatro es más cercano al primero
# Esta versión muestra TODOS los números que tienen la distancia mínima.

# Leer los cinco números enteros
n1 = int(input("Introduce el número 1 (referencia): "))
n2 = int(input("Introduce el número 2: "))
n3 = int(input("Introduce el número 3: "))
n4 = int(input("Introduce el número 4: "))
n5 = int(input("Introduce el número 5: "))

# Calcular las distancias de los cuatro últimos números al primero
distancia_n2 = abs(n2 - n1)
distancia_n3 = abs(n3 - n1)
distancia_n4 = abs(n4 - n1)
distancia_n5 = abs(n5 - n1)

# Guardar estas distancias en una lista
distancias = [distancia_n2, distancia_n3, distancia_n4, distancia_n5]

# Encontrar la distancia mínima en la lista de distancias
distancia_minima = min(distancias)

# Ahora, vamos a crear una lista para guardar todos los números que son más cercanos
numeros_mas_cercanos = []

# Comprobamos cada número individualmente con 'if'
if distancia_n2 == distancia_minima:
    numeros_mas_cercanos.append(n2) # Si n2 tiene la distancia mínima, lo añadimos a la lista

if distancia_n3 == distancia_minima:
    numeros_mas_cercanos.append(n3) # Si n3 tiene la distancia mínima, lo añadimos

if distancia_n4 == distancia_minima:
    numeros_mas_cercanos.append(n4) # Si n4 tiene la distancia mínima, lo añadimos

if distancia_n5 == distancia_minima:
    numeros_mas_cercanos.append(n5) # Si n5 tiene la distancia mínima, lo añadimos

# 6) Mostrar resultado
print("Número de referencia:", n1)
print("Candidatos:", n2, n3, n4, n5)

# Comprobamos cuántos números más cercanos hay para mostrar el mensaje adecuado
if len(numeros_mas_cercanos) == 1:
    print("El número más cercano al", n1, "es", numeros_mas_cercanos[0])
else:
    print("Los números más cercanos al", n1, "son:", numeros_mas_cercanos)