#11. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

# Pedimos al usuario un número y quitamos espacios por si escribe con espacios
n = input("Introduce un número de dos cifras: ").strip()

# Validamos: exactamente 2 caracteres y que sean dígitos
if len(n) == 2 and n.isdigit():
    # Invertimos la cadena con slicing (paso -1)
    invertido = n[::-1]
    # Mostramos el resultado
    print("Número invertido: " + invertido)
else:
    print("Solo dos dígitos (00–99).")