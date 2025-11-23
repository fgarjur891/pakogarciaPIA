import numpy as np

precios = np.random.randint(10,61,15)
ventas = np.random.randint(0,101,15)

ingresos = precios * ventas
ventas_max = ventas.max()
pos_max = ingresos.argmax()

print("Precios:", precios)
print("Ventas:", ventas)
print("Ingresos por producto:", ingresos)
print(f"Ventas máximas:, {ventas_max} posición {pos_max} Precio Juego: {precios[pos_max]} ")

count_  = (precios < 30) & (ventas > 50)
print ("Número de productos con ingresos < 30 y > 50:", count_.sum())

