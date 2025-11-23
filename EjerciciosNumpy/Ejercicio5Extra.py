import numpy as np


# --- CLASE PADRE ---
class Dado:
    def __init__(self, caras):
        self.caras = caras

    def tirar(self):
        return np.random.randint(1, self.caras + 1)


# --- CLASE HIJA 1: PARCHÍS (Perfecta) ---
class Dadoparchis(Dado):
    def __init__(self):
        super().__init__(6)
        # Hereda el método tirar() del padre tal cual


# --- CLASE HIJA 2: POKER (Corregida) ---
class Dadopoker(Dado):
    def __init__(self):
        super().__init__(6)  # Al padre le decimos que tiene 6 caras (número)
        # Las figuras las guardamos en una variable propia de esta clase
        self.figuras = ["AS", "K", "Q", "J", "R", "N"]

    def tirar(self):
        # Sobrescribimos: Ignoramos al padre y elegimos una figura al azar
        return np.random.choice(self.figuras)


# --- CLASE HIJA 3: TRUCADO (Lo que necesitas) ---
class Dadotruc(Dado):
    def __init__(self):
        super().__init__(6)
        # Definimos las opciones posibles
        self.opciones = [1, 2, 3, 4, 5, 6]

        # Definimos las probabilidades (El "truco")
        # Fíjate que el último (el 6) tiene 0.5 (50%) de probabilidad
        # Los demás se reparten el otro 50% (0.1 cada uno)
        # IMPORTANTE: Todo esto debe sumar 1.0
        self.probabilidades = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]

    def tirar(self):
        # Usamos choice pasando las opciones y el parámetro p (probabilidades)
        return np.random.choice(self.opciones, p=self.probabilidades)


# --- ZONA DE PRUEBAS ---
if __name__ == "__main__":
    mi_dado_trucado = Dadotruc()
    mi_dado_parchis = Dadoparchis()
    mi_dado_poker = Dadopoker()

    print("Tirando dados 10 veces:")
    for i in range(10):
        print(mi_dado_trucado.tirar(), mi_dado_parchis.tirar(), mi_dado_poker.tirar(), end=" ")