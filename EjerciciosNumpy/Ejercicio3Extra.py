import numpy as np


ciudad_A = np.random.randint(10,36,10)
ciudad_B = np.random.randint(10,36,10)

diferencia = ciudad_A - ciudad_B
mas_calor_a = 0
mas_calor_a = np.sum(ciudad_A > ciudad_B)


print("Días con más calor en la ciudad A que en la ciudad B:", mas_calor_a)
