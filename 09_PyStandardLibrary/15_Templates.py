# 4'53

# u videu 14 kompozicija coda za slanje email-a imala je body-texta i text. Medjutim, realworld mail imaju puno vise sadrzaja i pisati ih ovdje zajedno nije prakticno.
# Puno cesca praksa je da se ti body-djelovi stavljaju u posebne fajlove-templates-e.
# Za templates-e koristimo HTML, ovdje kreiramo u root-mapi prijekta fajl "template.html" cisto radi demoa inace.
# U stvarnoj aplikaciji cesto imamo razlicite templatese za razne scenarije: users-signup, password-reset attempt, order itd i imena template-fajlova dajemo prema tim scenarijima.
# cool-tehnic za brzo generiranje html-koda: ! i EmetAbr
# Za email nam unutar header-a nista ne treba pa brise! Tekst emaila ide u body-tag. "Hi user..." Sad nam pokazuje kako imati platz-holder u html: $name
# Potom ide u app i dodaje red za importanje Template-a. Ja vracam sav app-sadrzaj! iz 14 u app i pripremam za 15.
# Kreiramo objekt "template" od Template klase i koristimo metod substitute i stavljamo ga na mjesto "BodyAJ", sto kasnije on korigira i pravi posebnu varijablu "body"
# nakon novog uspjesnog slanja vraca se u template i stavlja oko imena tag <strong> sto bolda ime usera!
# jos malo o mogucnostima metoda "substitute" i "kwarg"-sima tako da umjesto dicta unacimo kwarg "name="Antun""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "Antun Jerkovic"
message["to"] = "evica.jerkovic@gmail.com"
message["subject"] = "This is my AJ test"
#body = template.substitute({"name": "Antun"})
body = template.substitute(name="Antun")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("beauty.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("antun.jerkovic@peta-brzina.hr", "a1j2p3b4")
    smtp.send_message(message)
    print("Sent...")
