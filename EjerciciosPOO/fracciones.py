"""
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominador cero.
Las fracciones pueden operar entre sí.
Sumar, multiplicar, dividir, restar.
Ojo!!! esto se puede hacer: f + 1, 5 * f
Las fracciones se pueden comparar.
==, <, <=, >, >=, !=
Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
Ojo!!! esto se puede hacer 1 < 1/2
Francisco José García Jurado
"""

import math


class Fraction:

    def __init__(self, numerator, denominator=1):
        """
        Constructor de la fracción.
        Guarda los valores y llama a __normalize() para "arreglarlos".
        """
        # REQUISITO: No se puede tener un denominador cero.
        if denominator == 0:
            raise ValueError("El denominador no puede ser cero")

        # 1. Guardamos los valores "en sucio" (tal como llegan)
        self.__numerator = numerator
        self.__denominator = denominator

        # 2. Llamamos a normalize() para que "limpie" el objeto
        self.__normalize()

    def __normalize(self):
        """
        Modifica los atributos internos para que estén en el rango adecuado.
        Para una fracción, "normalizar" es:
        1. Simplificar (ej: 2/4 -> 1/2) usando el Máximo Común Divisor (MCD).
        2. Asegurar que el signo esté en el numerador (ej: 1/-2 -> -1/2).
        """

        # 1. Simplificar usando el Máximo Común Divisor (MCD o 'gcd')
        common = math.gcd(self.__numerator, self.__denominator)
        self.__numerator //= common
        self.__denominator //= common

        # 2. Mover el signo al numerador
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    # --- Propiedades ---
    # Damos acceso de solo lectura
    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        if self.__denominator == 1:
            return f"{self.__numerator}"
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        return f"Fraction({self.__numerator}, {self.__denominator})"

    def _get_value(self):
        """
        Es nuestra "unidad base" para comparar. Devolvemos el valor decimal.
        """
        return self.__numerator / self.__denominator

    def __eq__(self, other):
        """ REQUISITO: == (igual que) """

        # REQUISITO: 1/2 == 2/4
        # ¡La normalización ya ha resuelto esto!
        # Fraction(1, 2) se normaliza y se guarda como (1, 2)
        # Fraction(2, 4) se normaliza y se guarda como (1, 2)
        # ¡Así que solo tenemos que comparar los atributos internos!

        if isinstance(other, Fraction):
            return (self.__numerator == other.__numerator and
                    self.__denominator == other.__denominator)

        # REQUISITO: Comparar con números (ej: Fraction(4, 2) == 2)
        if isinstance(other, (int, float)):
            return self._get_value() == other

        return NotImplemented

    def __lt__(self, other):
        """ REQUISITO: < (menor que) """
        # Usamos nuestra "unidad base" _get_value()

        if isinstance(other, Fraction):
            return self._get_value() < other._get_value()

        # REQUISITO: Comparar con números (ej: 1 < Fraction(3, 2))
        if isinstance(other, (int, float)):
            return self._get_value() < other

        return NotImplemented

    # Definimos el resto
    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other

    # --- Operaciones Aritméticas ---

    def __add__(self, other):
        """ REQUISITO: Suma (f + g) y (f + 1) """

        # REQUISITO: f + 1
        # Comprobamos si 'other' es un número
        if isinstance(other, int):
            # Si es un número, lo tratamos como una fracción
            other = Fraction(other, 1)

        if isinstance(other, Fraction):
            # Matemática de fracciones: a/b + c/d = (ad + bc) / bd
            new_num = (self.__numerator * other.__denominator) + \
                      (other.__numerator * self.__denominator)
            new_den = self.__denominator * other.__denominator

            # ¡Devolvemos una NUEVA fracción!
            # Esta nueva fracción se auto-normalizará en su __init__
            return Fraction(new_num, new_den)

        return NotImplemented

    def __radd__(self, other):
        """ REQUISITO: Suma "refleja" (ej: 1 + f) """
        # Esto se llama si Python intenta 1 + f (y '1' no sabe)
        # Le damos la vuelta, y nuestro __add__ ya sabe manejarlo.
        return self + other

    def __sub__(self, other):
        """ REQUISITO: Resta (f - g) y (f - 1) """
        if isinstance(other, int):
            other = Fraction(other, 1)

        if isinstance(other, Fraction):
            # Matemática de fracciones: a/b - c/d = (ad - bc) / bd
            new_num = (self.__numerator * other.__denominator) - \
                      (other.__numerator * self.__denominator)
            new_den = self.__denominator * other.__denominator
            return Fraction(new_num, new_den)

        return NotImplemented

    def __rsub__(self, other):
        """ REQUISITO: Resta "refleja" (ej: 1 - f) """
        # 1 - f no es f - 1, así que lo calculamos bien
        other_fraction = Fraction(other, 1)
        return other_fraction - self

    def __mul__(self, other):
        """ REQUISITO: Multiplicación (f * g) y (f * 5) """
        if isinstance(other, int):
            other = Fraction(other, 1)

        if isinstance(other, Fraction):
            # Matemática de fracciones: (a/b) * (c/d) = ac / bd
            new_num = self.__numerator * other.__numerator
            new_den = self.__denominator * other.__denominator
            return Fraction(new_num, new_den)

        return NotImplemented

    def __rmul__(self, other):
        """ REQUISITO: Multiplicación "refleja" (ej: 5 * f) """
        # La multiplicación sí es conmutativa (5*f = f*5)
        return self * other

    def __truediv__(self, other):
        """ REQUISITO: División (f / g) y (f / 5) """
        if isinstance(other, int):
            other = Fraction(other, 1)

        if isinstance(other, Fraction):
            if other.__numerator == 0:
                raise ZeroDivisionError("División por una fracción cero")

            # Matemática de fracciones: (a/b) / (c/d) = ad / bc
            new_num = self.__numerator * other.__denominator
            new_den = self.__denominator * other.__numerator
            return Fraction(new_num, new_den)

        return NotImplemented

    def __rtruediv__(self, other):
        """ REQUISITO: División "refleja" (ej: 5 / f) """
        other_fraction = Fraction(other, 1)
        return other_fraction / self