# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
# Si introducimos otro número nos da un error.

# Lista de días
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Pedir número de día
numero_dia = int(input("Introduce el número del día de la semana (del 1 al 7): "))

# Validar y ajustar índice restando 1
if numero_dia >= 1 and numero_dia <= 7:
    indice = numero_dia - 1   # Convertimos 1..7 -> 0..6
    print("El día correspondiente es:", dias_semana[indice])
else:
    print("Error: Número introducido no válido. Debe ser un número del 1 al 7.")