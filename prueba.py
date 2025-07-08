import send_email

sender = "simon.marquezok@gmail.com"
sender_token = "lpgr szsn ydle fmsd"
recipient = "msimonz1@hotmail.com"
cobro_pdf = "/Users/simonmarquez/Dropbox/Simon/TRABAJO/Cetus/2025/Pagos/Mayo/CuentadeCobro.pdf"
files = {}
files["CuentadeCobro"] = cobro_pdf
for file, path in files.items():
    print(path)
#send_email.send_email(recipient, sender, sender_token, "Mayo", cobro_pdf)