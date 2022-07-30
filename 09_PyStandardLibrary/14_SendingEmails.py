# 6'48

# treba importati nekoliko klasa: za pravljenje maila, za povezivanje sa smtp-iom itd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

# email -paket u PyStandard library; mime je podpaket "multipurpose internet mail extension" i standard je koji definira format za email-poruke, nema nista sa Py, opci standard; multipart je podpaket od mime koji nam donosi klasu MIMEMultipart
# objekti ove klase mogu slati emailove koji sadrze i HTML i obicni tekst tj ako receiver prima text dobice text inace html!!

# idemo sada kreirati MIMEMultipart objekt
message = MIMEMultipart()
# potom kreiramo razne Headere!
message["from"] = "Antun Jerkovic"
message["to"] = "evica.jerkovic@gmail.com"
message["subject"] = "This is my AJ test"

# da bi mogli imati body mail-a moramo importati novi klass MIMEText
# ako zelimo da je BodyAJ html moramo dodati drugi arg "html" ali aako je obican tekst ne treba nista!
message.attach(MIMEText("BodyAJ"))
message.attach(MIMEImage(Path("beauty.png").read_bytes()))

# sad treba importati modul za smpt server i protokol a potom
# ? smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
# na kraju bi trebalo pripaziti da se objekt zatvori i oslobode resursi sa
# ? smtp.close()
# ali Ath radje bira to sa "with" pa umjesto "smtp = ..."  imamo
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # malo promjenjen Hello za pocetak koma klijent-server
    smtp.starttls()  # stavlja smtp-konekciju u tls-mod (transport-layer-security) tj u enkripciju
    smtp.login("antun.jerkovic@peta-brzina.hr", "a1j2p3b4")
    smtp.send_message(message)
    print("Sent...")
# problem - google-mail ne da vise!
# za kraj Ath pokazuje atachiraje Image-ea poruci!
