# 5'09

from email import message


def greet(name):
    message = "a"

# ? print(a)        # NameError: name 'a' is not defined


def send_email(name):
    message = "b"


greet("Mosh")

# garbage -collector, py lokalne varijable brise iz memorije!
# Osim lokalnih imamo i globalne varijable koje su na identation-level 0! i koje u memoriji stoje duze vremena! Ali zato su very evel i ne bi ih trebali koristiti very offten.

message = "a"


def greet(name):
    message = "b"


greet("Mosh")

print(message)  # a samo globalnu, do lokalne ne dopire!

# do lokalne se ne dopire ali ni funkcija do globalne, da bi mogla, unutar funs dodajemo "global message" sto je potrebno interpretery da inicijalizira varijablu, a red ispod joj odmah mjenja vrijednost sa "a" na "b" pa zato "b"

message = "a"


def greet(name):
    global message
    message = "b"


greet("Mosh")

print(message)  # b

# losa strana globalnih je upravo u njihovoj vezi sa vise funkcija od kojih neke mogu i izmjeniti njenu vrijednost (kao u primjeru) sto poslije ima nenamjeravane posljedice na druge funkcije. To je negativna posljedica koja se ne odnosi samo na Py, nego i na druge i postoji diskusija destljecima. Izbjegavajmo ih! Ako bas trebaju nek to bude primjer nj. citanja ali ne modificiranja!
