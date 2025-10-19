# Tabla de multiplicar completa
# Pide al usuario un número entre 1 y 10, y muestra su tabla de multiplicar.
# Después de mostrarla, pregunta si quiere ver otra tabla.
# El programa continúa hasta que el usuario diga “no”.
# Autor: Francisco José García Jurado
request = "si"
while request == "si":
    number = int(input("Ingrese un numero y te muestro la tabla del multiplicar: "))
    print("Tabla del multiplicar del ", number)
    for i in range (10):
        print(f"{number} x {i + 1} = {number * (i + 1)}")

    request = input("Quieres que te muestre otra tabla? ").strip().lower()
    while request != "si" and request != "no":
        request = input("Dime si o no ").strip().lower()
