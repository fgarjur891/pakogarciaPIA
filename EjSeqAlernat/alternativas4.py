# Programa para clasificar un carácter introducido por teclado.

# Definimos cadenas con todos los signos de puntuación
# Incluimos los signos de puntuación comunes
# Definimos cadenas con las letras (mayúsculas, minúsculas y acentuadas)
# Definimos una cadena con los dígitos

signos_puntuacion = ".,;:!¡¿?-_" 
letras_minusculas = "abcdefghijklmnñopqrstuvwxyzáéíóúü"
letras_mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
digitos = "0123456789"

entrada = input("Introduce un carácter: ")

# Comprobamos primero si ha introducido más de un carácter o ninguno
if len(entrada) != 1:
    print("No es un carácter")
else:

    # Comprobamos si es una letra (mayúscula, minúscula o acentuada)
    if letras_minusculas.find(entrada) != -1 or letras_mayusculas.find(entrada) != -1:
        print("Es una letra")
    # Comprobamos si es un dígito
    elif digitos.find(entrada) != -1:
        print("Es un dígito")
    # Comprobamos si es un signo de puntuación
    elif entrada.find(signos_puntuacion) != -1:
        print("Es signo de puntuación")
    else:
        # Si no es ninguno de los anteriores
        print("Es otro carácter")