"""Ejercicio 1

En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable. Debe permitir:

Crear duraciones de tiempos.
Ejemplo: t = Duration(10,20,56)
Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
Si no indico la hora, minuto o segundo estos valores son cero:
Duration() --> (0, 0, 0)
Duration(34) --> (34, 0, 0)
Duration(34, 15) --> (34, 15, 0)
Duration(34, 61) --> (35, 1, 0)
Las duraciones de tiempo se pueden comparar.
A las duraciones de tiempo les puedo sumar y restar segundos.
Las duraciones de tiempo se pueden sumar y restar. """


# --- Definición de la Clase ---
# Creamos una nueva clase llamada 'duration' para manejar tiempos.
class duration():

    # --- 1. El Constructor (__init__) ---
    # Este método se llama automáticamente CADA VEZ que creamos un nuevo objeto duration().
    # Su trabajo es recibir los datos iniciales y configurar el objeto.
    def __init__(self, hours=0, minutes=0, seconds=0):

        # --- 1a. Validación ---
        # Primero, comprobamos si los datos de entrada son válidos.
        # Si alguno no es un número entero, detenemos todo y lanzamos un error.
        if not isinstance(hours, int) or not isinstance(minutes, int) or not isinstance(seconds, int):
            raise TypeError("Las datos deben ser enteros")

        # --- 1b. Normalización ---
        # Si los datos son válidos, los "normalizamos".
        else:
            # 1. Convertimos TODO a la unidad más pequeña (segundos).
            #    Esto maneja automáticamente casos como (10, 62, 15).
            total_seconds = hours * 3600 + minutes * 60 + seconds

            # 2. Guardamos los valores "repartidos" en variables "privadas".
            #    Estas variables (__hours) son el almacenamiento interno real.
            self.__hours = total_seconds // 3600
            self.__minutes = (total_seconds % 3600) // 60
            self.__seconds = total_seconds % 60

    # --- 2. Propiedades (Getters) ---
    # Estas funciones (@property) nos permiten "leer" los valores privados
    # de forma segura, pero (al no tener @setter) no nos dejan modificarlos.
    # Esto hace que la clase sea INMUTABLE.

    @property
    def hours(self):
        # Devuelve el valor de la variable privada __hours.
        return self.__hours

    @property
    def minutes(self):
        # Devuelve el valor de la variable privada __minutes.
        return self.__minutes

    @property
    def seconds(self):
        # Devuelve el valor de la variable privada __seconds.
        return self.__seconds

    @property
    def total_seconds(self):
        # Es una propiedad de "solo lectura" que calcula el valor total
        # de la duración en segundos basándose en los datos ya guardados.
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    # --- 3. Métodos Mágicos (Comportamiento) ---

    # __str__ controla qué se muestra si hacemos print(mi_objeto)
    def __str__(self):  # para pasarlo a cadena
        # Usamos un f-string para formatearlo como H:M:S
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    # __add__ controla qué pasa cuando usamos el operador "+"
    def __add__(self, other):
        # 1. Sumamos los segundos totales de ambos objetos.
        total_seconds = self.total_seconds + other.total_seconds
        # 2. Creamos y devolvemos un objeto duration NUEVO.
        #    Le pasamos el total de segundos, y dejamos que __init__
        #    haga la normalización automáticamente.
        return duration(seconds=total_seconds)

    # __sub__ controla qué pasa cuando usamos el operador "-"
    def __sub__(self, other):
        # 1. Restamos los segundos totales.
        total_seconds = self.total_seconds - other.total_seconds
        # 2. Creamos y devolvemos un objeto duration NUEVO,
        #    dejando que __init__ se encargue de normalizarlo.
        return duration(seconds=total_seconds)

    # --- 4. Métodos Mágicos (Comparación) ---
    # Todos estos se basan en la "llave maestra" (total_seconds)
    # para hacer comparaciones simples y 100% correctas.

    # __lt__ controla el operador "<" (Menor que)
    def __lt__(self, other):
        return self.total_seconds < other.total_seconds

    # __eq__ controla el operador "==" (Igual a)
    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    # __gt__ controla el operador ">" (Mayor que)
    def __gt__(self, other):
        return self.total_seconds > other.total_seconds

    # __le__ controla el operador "<=" (Menor o igual que)
    def __le__(self, other):
        return self.total_seconds <= other.total_seconds

    # __ge__ controla el operador ">=" (Mayor o igual que)
    def __ge__(self, other):
        return self.total_seconds >= other.total_seconds

    # --- 5. Métodos Personalizados ---
    # Estos no son "mágicos", son funciones que creamos para cumplir requisitos.

    # Permite sumar un número (int) de segundos a la duración
    def __addseconds__(self, other):
        # 'other' aquí es un número entero (ej: 30)
        # 1. Sumamos el número al total de segundos.
        # 2. Devolvemos un objeto duration NUEVO, dejando que __init__ normalice.
        return duration(seconds=self.total_seconds + other)

    # Permite restar un número (int) de segundos a la duración
    def __subseconds__(self, other):
        # 'other' aquí es un número entero (ej: 30)
        # 1. Restamos el número del total de segundos.
        # 2. Devolvemos un objeto duration NUEVO.
        return duration(seconds=self.total_seconds - other)