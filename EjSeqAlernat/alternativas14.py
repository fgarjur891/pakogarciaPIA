# Diseña un programa que, dado un número real que debe representar 
# la calificación numérica de un examen, proporcione 
# la calificación cualitativa correspondiente al número dado. 
# La calificación cualitativa será una de las siguientes: 
# «Suspenso» (nota menor que 5), 
# «Aprobado» (nota mayor o igual que 5, pero menor que 7), 
# «Notable» (nota mayor o igual que 7, pero menor que 9), 
# «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), 
# «Matrícula de Honor» (nota 10)

# Pedimo nota calificación

nota = float(input("Dame nota a evaluar: "))

# Comprobamos nota válida
if nota <0 or nota>10:
    print("Nota no válida")
else: # con nota válida comprobamos distintos grupos
    if nota < 5:
        print("Suspenso")
    elif nota < 7:
        print("Aprobado")
    elif nota < 9:
        print("Notable")
    elif nota < 10:
        print("Sobresaliente")
    elif nota == 10:
        print("Matricula de honor")

