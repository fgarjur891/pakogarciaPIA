# 10. Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
# Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, 
# ¿cómo se puede calcular?

#El programa mostrara la raiz cuadrada y cubica si es positivo
#Si es negativo dirá que la raiz cuadrada es imaginaria y calcula solo la cubica

number = float(input("Dime un número: "))
# Compruebo si el número es positivo (cero incluido) o negativo
if number >= 0:
    print("La raiz cuadrada es: ", number ** (1/2))
    print("La raiz cúbica es:", number ** (1/3))
else:
    print("La raiz cuadrada es imaginaria")

# Realizo el cálculo con el valor absoluto (sino me genera numero notacion) y luego pongo negativo
    print("La raiz cúbica es ",-(abs(number) ** (1/3)))

