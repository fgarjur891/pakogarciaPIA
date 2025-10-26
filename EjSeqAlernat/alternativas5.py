# Programa para determinar el tipo de triángulo según las longitudes de sus lados

print ("Calculamos tipo de triángulo")

side_a = float(input("Introduce la longitud del lado A: "))
side_b = float(input("Introduce la longitud del lado B: "))
side_c = float(input("Introduce la longitud del lado C: "))


if not (side_a + side_b > side_c and
        side_a + side_c > side_b and
        side_b + side_c > side_a):
    print("Con estas longitudes, no se puede formar un triángulo válido.")
else:
    # 3) Ordenar lados para identificar la hipotenusa (el mayor)
    lados_ordenados = sorted([side_a, side_b, side_c])
    cateto1 = lados_ordenados[0]
    cateto2 = lados_ordenados[1]
    hipotenusa = lados_ordenados[2]

    suma_catetos = round(cateto1**2 + cateto2**2, 3)
    cuadrado_hipo = round(hipotenusa**2, 3)

    if suma_catetos == cuadrado_hipo:
        # Si son exactamente iguales tras redondear, consideramos que cumple Pitágoras
        print("Es un triángulo rectángulo.")

    if side_a == side_b and side_b == side_c:
        print("Es un triángulo equilátero.")
    # 6) Isósceles: exactamente dos lados iguales
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        print("Es un triángulo isósceles.")
    # 7) Escaleno: todos distintos
    else:
        print("Es un triángulo escaleno.")