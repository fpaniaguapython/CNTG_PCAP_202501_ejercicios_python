import datetime

hoy = datetime.date.today() # Obtenemos en date de hoy
print(hoy)
print(hoy.year)
print(hoy.month)
print(hoy.day)

fin_anyo = datetime.date(2025, 12, 31)

import time

ahora_mismo = time.time()
print(ahora_mismo) # 1738954146.192879

ahora = datetime.date.fromtimestamp(ahora_mismo) # A partir del timestamp, se obtiene la fecha
print(ahora)

print(ahora.weekday()) # 4 (es viernes)

import datetime

hoy_y_ahora = datetime.datetime.now()
datetime.datetime.utcnow() # Utilizar now indicando el UTC (ver documentación)


# timedelta permite crear un 'delta' de desplazamiento para sumar o restar a una fecha
desplazamiento = datetime.timedelta(days=50, seconds=0, microseconds=0,
milliseconds=0, minutes=0, hours=0, weeks=0)

print(hoy_y_ahora) # 2025-02-07 20:02:02.057487
print(hoy_y_ahora+desplazamiento)#2025-03-29 20:04:34.137452

import calendar
print(calendar.month(2025,2))