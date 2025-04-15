from email.mime.application import MIMEApplication
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(recipient, sender, sender_password, mes, file_route):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = 'Cuenta de Cobro y Planilla {mes}'.format(mes=mes)
    with open(file_route, "rb") as f:
        attached_file = MIMEApplication(f.read(), Name=os.path.basename(file_route))
        attached_file['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_route)}"'
        msg.attach(attached_file)
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(sender, sender_password)
        servidor.sendmail(sender, recipient, msg.as_string())
        servidor.quit()
        print("✅ Correo con adjunto enviado")
    except Exception as e:
        print("❌ Error:", e)