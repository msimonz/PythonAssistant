from email.mime.application import MIMEApplication
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(recipient, sender, sender_token, mes, file_route):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = 'Cuenta de Cobro y Planilla {mes}'.format(mes=mes)
    for file, path in file_route.items():
        with open(path, "rb") as f:
            attached_file = MIMEApplication(f.read(), Name=os.path.basename(path))
            attached_file['Content-Disposition'] = f'attachment; filename="{os.path.basename(path)}"'
            msg.attach(attached_file)
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(sender, sender_token)
        servidor.sendmail(sender, recipient, msg.as_string())
        servidor.quit()
        print("✅ Correo con adjunto enviado")
    except Exception as e:
        print("❌ Error:", e)