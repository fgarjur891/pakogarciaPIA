# Funciones 1. Menu operaciones
# Autor: Francisco José García Jurado



# --- 1. DEFINICIÓN DE FUNCIONES ---

def sum_(num1, num2):
    return num1 + num2

def subtract_(num1, num2):
    return num1 - num2

def multiply_(num1, num2):
    return num1 * num2

def divide_(num1, num2):
    return num1 / num2

def get_number():
    return float(input("Ingresa un número: "))

def choose_functions(options_list):
    option_menu = 0
    print ("***** Menú de opciones *****")
    for i in range(len(options_list)):
        print(f"Opción {i} -- {options_list[i]}")

    while True:
        try:
            option_menu = int(input(f"Introduce una opción (0-{len(options_list)-1}): "))
            if option_menu >= 0 and option_menu <= len(options_list)-1:
                return option_menu
            else:
                print ("La opción no es válida")
        except ValueError:
                print (f"Debes introducir solo dígitos entre el 0 y {len(options_list)-1} ")

def main():
    number1 = 0
    number2 = 0
    sw = False

    while True:

        option_menu = choose_functions(["Salir", "Pedir Números", "Suma", "Resta", "Multiplicación", "Division"])

        match option_menu:
            case 0:
                print("Gracias ¡Hasta luego!")
                break
            case 1:
                number1 = get_number()
                number2 = get_number()
                sw = True
            case 2 | 3 | 4 | 5:
                if sw == True:
                    if option_menu == 2:
                        print("El resultado de la suma es: ", sum_(number1, number2))
                    elif option_menu == 3:
                        print("El resultado de resta es: ", subtract_(number1, number2))
                    elif option_menu == 4:
                        print("El resultado de multiplicación es: ", multiply_(number1, number2))
                    elif option_menu == 5:
                        if number2 == 0:
                            print("Error: No se puede dividir por cero.")
                        else:
                            print("El resultado de division es: ", divide_(number1, number2))
                else:
                    print("No has introducido ningún número")
            case _:
                print("Error inesperado")



main()
