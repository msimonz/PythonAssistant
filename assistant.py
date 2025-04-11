import shutil
import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
mes_actual_num = datetime.now().month
anio_actual = datetime.now().year
mes_actual = datetime.now().strftime("%B").capitalize()
print(type(mes_actual_num))

def encontrar_fecha(anio_siguiente, mes_siguiente):
    fecha_siguiente = datetime(anio_siguiente, mes_siguiente, 1)
    nombre_mes_siguiente = fecha_siguiente.strftime("%B").capitalize()
    origin = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/Prueba/{mes_actual}".format(mes_actual=mes_actual)
    print(origin)
    destination = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/Prueba/{nombre_mes_siguiente}".format(nombre_mes_siguiente=nombre_mes_siguiente)
    print(destination)
    return origin, destination

def crear_carpeta_cambio_de_anio(origin, destination):
    print("Cambio de año")

def crear_carpeta_cambio_de_mes(origin, destination):
    print("Cambio de mes")
    if shutil.copytree(origin, destination) :
        print("Carpeta copiada")


if mes_actual_num == 12:
    mes_siguiente = 1
    anio_siguiente = anio_actual + 1
    origin, destination = encontrar_fecha(anio_siguiente, mes_siguiente)
    crear_carpeta_cambio_de_anio(origin, destination)
    
else:
    mes_siguiente = mes_actual_num + 1
    anio_siguiente = anio_actual
    origin, destination = encontrar_fecha(anio_siguiente, mes_siguiente)
    crear_carpeta_cambio_de_mes(origin, destination)



