import numpy as np

numbers = np.arange(1,37)

array_numbers = numbers.reshape(6,6)

centro = array_numbers[2:4,2:4]

# Asignamos el valor 0 a todas esas posiciones a la vez
array_numbers[0,0] = array_numbers[0,5] = array_numbers[5,0] = array_numbers[5,5] = 0

# ::5 significa "toda la lista, saltando de 5 en 5"
# Como la matriz es de 6x6, cogerá el índice 0 y el 5.
#rray_numbers[::5, ::5] = 0

print(array_numbers)
print(centro)