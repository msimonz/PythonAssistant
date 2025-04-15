import os
import shutil
import locale
from datetime import datetime
from openpyxl import load_workbook
import calendar
import convert_to_pdf
import send_email

def encontrar_fecha(anio_siguiente, mes_siguiente, anio_actual):
    fecha_siguiente = datetime(anio_siguiente, mes_siguiente, 1)
    nombre_mes_siguiente = fecha_siguiente.strftime("%B").capitalize()
    origin = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_actual}/Prueba/{mes_actual}".format(mes_actual=mes_actual, anio_actual=anio_actual)
    print(origin)
    destination = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_actual}/Prueba/{nombre_mes_siguiente}".format(nombre_mes_siguiente=nombre_mes_siguiente, anio_actual = anio_actual)
    print(destination)
    return origin, destination, nombre_mes_siguiente

def crear_carpeta_cambio_de_anio(anio_actual, mes_siguiente, cuenta_de_cobro, formato_de_aprobacion):
    print("cambio de anio")
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
    modificar_archivos(cuenta_de_cobro, formato_de_aprobacion, nombre_mes_siguiente, anio_siguiente)

def crear_carpeta_cambio_de_mes(destination, cuenta_de_cobro, formato_de_aprobacion, nombre_mes_siguiente):
    print("Cambio de mes")
    os.mkdir(destination)
    if os.path.exists(destination):
        print("Carpeta creada")
    else:
        print("Carpeta no creada")
    modificar_archivos(cuenta_de_cobro, formato_de_aprobacion, nombre_mes_siguiente, anio_actual)


def modificar_archivos(cuenta_de_cobro, formato_de_aprobacion, nombre_mes_siguiente, anio):
    print("Modificando archivos")
    cobro = load_workbook(cuenta_de_cobro)
    aprobacion = load_workbook(formato_de_aprobacion)
    cobro_sheet = cobro.active
    aprobacion_sheet = aprobacion.active
    _, dias_mes_siguiente = calendar.monthrange(anio, mes_siguiente)
    if dias_mes_siguiente > 30:
        cobro_sheet["C15"] = "Días laborados desde el 01 al 31 de {nombre_mes_siguiente}".format(nombre_mes_siguiente=nombre_mes_siguiente)
        aprobacion_sheet["J7"] = "1 al 31 de {nombre_mes_siguiente}".format(nombre_mes_siguiente=nombre_mes_siguiente)
        numero = cobro_sheet["H3"]
        numero.value += 1
        cobro_sheet["H3"] = numero.value
    else:
        cobro_sheet["C15"] = "Días laborados desde el 01 al {dias_mes_siguiente} de {nombre_mes_siguiente}".format(dias_mes_siguiente=dias_mes_siguiente, nombre_mes_siguiente=nombre_mes_siguiente)
        aprobacion_sheet["J7"] = "1 al {dias_mes_siguiente} de {nombre_mes_siguiente}".format(dias_mes_siguiente=dias_mes_siguiente, nombre_mes_siguiente=nombre_mes_siguiente)
        numero = cobro_sheet["H3"]
        numero.value += 1
        cobro_sheet["H3"] = numero.value
    cobro.save(cuenta_de_cobro)
    aprobacion.save(formato_de_aprobacion)
    convert_to_pdf.excel_to_pdf(cuenta_de_cobro, cobro_pdf)
    convert_to_pdf.excel_to_pdf(formato_de_aprobacion, aprobacion_pdf)



locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
mes_actual_num = datetime.now().month
anio_actual = datetime.now().year
mes_actual = datetime.now().strftime("%B").capitalize()
print(type(mes_actual_num))
cuenta_de_cobro = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_actual}/Prueba/CuentadeCobro.xlsx".format(anio_actual=anio_actual)
formato_de_aprobacion = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/{anio_actual}/Prueba/FormatodeAprobacion.xlsx".format(anio_actual=anio_actual)
sender = "simon.marquezok@gmail.com"
sender_password = "mvva dwhv tlgn kikh"
recipient = "simon.marquezok@gmail.com"

#mes_actual_num = 12

if mes_actual_num == 12:
    mes_siguiente = 1
    anio_siguiente = anio_actual + 1
    origin, destination, nombre_mes_siguiente = encontrar_fecha(anio_siguiente, mes_siguiente, anio_actual)
    cobro_pdf = os.path.join(destination)
    aprobacion_pdf = os.path.join(destination)
    crear_carpeta_cambio_de_anio(anio_actual, nombre_mes_siguiente, cuenta_de_cobro, formato_de_aprobacion)
    send_email.send_email(recipient, sender, sender_password, nombre_mes_siguiente, cobro_pdf)
    send_email.send_email(recipient, sender, sender_password, nombre_mes_siguiente, aprobacion_pdf)

else:
    mes_siguiente = mes_actual_num + 1
    anio_siguiente = anio_actual
    origin, destination, nombre_mes_siguiente = encontrar_fecha(anio_siguiente, mes_siguiente, anio_actual)
    cobro_pdf = os.path.join(destination)
    aprobacion_pdf = os.path.join(destination)
    crear_carpeta_cambio_de_mes(destination, cuenta_de_cobro, formato_de_aprobacion, nombre_mes_siguiente)
    cobro_pdf = cobro_pdf + "/CuentadeCobro.pdf"
    aprobacion_pdf = aprobacion_pdf + "/FormatodeAprobacion.pdf"
    send_email.send_email(recipient, sender, sender_password, nombre_mes_siguiente, cobro_pdf)
    send_email.send_email(recipient, sender, sender_password, nombre_mes_siguiente, aprobacion_pdf)
    #os.rmdir(destination)



