# 12. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un programa que determine la hora de llegada a la ciudad B.
from idlelib.zoomheight import set_window_geometry

SECONDS_1MINUTE = 60
SECONDS_IN_HOUR = 3600

print("Introduzca horario de salida ")
hour_exit = int(input("Hora: "))
min_exit = int(input("Minutos: "))
seg_exit = int(input("Segundos: "))
print (" ")
time_travel = int(input("Introduce tiempo de viaje en segundos:"))

# Calculamos las H:M:S del tiempo introducido
seconds_hour = int(time_travel // SECONDS_IN_HOUR)
rest = int (time_travel % SECONDS_IN_HOUR)
seconds_minute = int(rest // SECONDS_1MINUTE)
seconds = int(rest % SECONDS_1MINUTE)

# Calculamos hora llegada

ss_final = seg_exit + seconds
mm_final = min_exit + seconds_minute
hh_final = hour_exit + seconds_hour

# Normalizamos resultado final
if ss_final>= SECONDS_1MINUTE:
    mm_final +=1
    ss_final -= SECONDS_1MINUTE
if mm_final>= SECONDS_1MINUTE:
    hh_final+=1
    mm_final-= SECONDS_1MINUTE
if hh_final>23:
    hh_final-=25

print("La hora de llegada es:",hh_final,":",mm_final,":",ss_final)