import os
import shutil
import locale
from datetime import datetime

def encontrar_fecha(anio_siguiente, mes_siguiente, anio_actual):
    fecha_siguiente = datetime(anio_siguiente, mes_siguiente, 1)
    nombre_mes_siguiente = fecha_siguiente.strftime("%B").capitalize()
    origin = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_actual}/Prueba/{mes_actual}".format(mes_actual=mes_actual, anio_actual=anio_actual)
    print(origin)
    destination = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_actual}/Prueba/{nombre_mes_siguiente}".format(nombre_mes_siguiente=nombre_mes_siguiente, anio_actual = anio_actual)
    print(destination)
    return origin, destination, nombre_mes_siguiente

def crear_carpeta_cambio_de_anio(anio_actual, mes_siguiente):
    cuenta_de_cobro = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/Pagos/CuentadeCobro.xlsx"
    formato_de_aprobacion = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/Pagos/FormatodeAprobacion.xlsx"
    print("Cambio de año")
    anio_siguiente = anio_actual + 1
    os.mkdir(f"/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_siguiente}")
    os.mkdir(f"/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_siguiente}/Prueba")
    os.mkdir(f"/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_siguiente}/Prueba/{mes_siguiente}")
    if shutil.copy(cuenta_de_cobro, f"/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_siguiente}/"):
        print("Cuenta de cobro copiada")
    else:    
        print("Cuenta de cobro no copiada")
    if shutil.copy(formato_de_aprobacion, f"/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_siguiente}/"):
        print("Formato de aprobacion copiado")
    else:
        print("Formato de aprobacion no copiado")

def crear_carpeta_cambio_de_mes(destination):
    print("Cambio de mes")
    os.mkdir(destination)
    if os.path.exists(destination):
        print("Carpeta creada")
    else:
        print("Carpeta no creada")

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
mes_actual_num = datetime.now().month
anio_actual = datetime.now().year
mes_actual = datetime.now().strftime("%B").capitalize()
print(type(mes_actual_num))

mes_actual_num = 12

if mes_actual_num == 12:
    mes_siguiente = 1
    anio_siguiente = anio_actual + 1
    origin, destination, nombre_mes_siguiente = encontrar_fecha(anio_siguiente, mes_siguiente, anio_actual)
    crear_carpeta_cambio_de_anio(anio_actual, nombre_mes_siguiente)
else:
    mes_siguiente = mes_actual_num + 1
    anio_siguiente = anio_actual
    origin, destination, nombre_mes_siguiente = encontrar_fecha(anio_siguiente, mes_siguiente, anio_actual)
    crear_carpeta_cambio_de_mes(destination)



