import shutil
import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
mes_actual_num = datetime.now().month
anio_actual = datetime.now().year
mes_actual = datetime.now().strftime("%B").capitalize()
print(type(mes_actual_num))

#mes_actual_num = 12

def encontrar_fecha(anio_siguiente, mes_siguiente, year_change):
    fecha_siguiente = datetime(anio_siguiente, mes_siguiente, 1)
    nombre_mes_siguiente = fecha_siguiente.strftime("%B").capitalize()
    origin = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/Prueba/{mes_actual}".format(mes_actual=mes_actual)
    print(origin)
    destination = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/Prueba/{nombre_mes_siguiente}".format(nombre_mes_siguiente=nombre_mes_siguiente)
    year ="/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/"
    year_duplicate = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/{anio_siguiente}".format(anio_siguiente=anio_siguiente)
    print(destination)
    print(year_duplicate)
    print(year)
    if year_change:
        return year, year_duplicate, origin, destination
    else:
        return origin, destination

def crear_carpeta_cambio_de_anio(origin, destination, year_duplicate, year):
    print("Cambio de año")

def crear_carpeta_cambio_de_mes(origin, destination):
    print("Cambio de mes")
    if shutil.copytree(origin, destination) :
        print("Carpeta copiada")


if mes_actual_num == 12:
    mes_siguiente = 1
    anio_siguiente = anio_actual + 1
    year, year_duplicate, origin, destination = encontrar_fecha(anio_siguiente, mes_siguiente, True)
    crear_carpeta_cambio_de_anio(origin, destination, year_duplicate, year)
    
else:
    mes_siguiente = mes_actual_num + 1
    anio_siguiente = anio_actual
    origin, destination = encontrar_fecha(anio_siguiente, mes_siguiente, False)
    crear_carpeta_cambio_de_mes(origin, destination)



