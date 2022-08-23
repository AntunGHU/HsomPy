# 2'55

# tj izvodjenje modula kao glavnog fajla!!!
# opet Ath u "sales.py" modulu u kom imamo 2 funkcije
# ali mozemo imati i bilo koji statement koji ce biti izvrsen prvi puta kad se modul ucitava!
# kao primjer daje liniju "print("Sales initialized")"
# ako sada izvedemo fajl npr app.py-a u kojem je sales importan, taj dio se pojavljuje na output-u!! tj sales je inicijaliziran!!
# koristeci isti nacin mozemo tako inicijalizirati nase pakete
# ath ide sa csp u komand-paletu i kuca  u __init__.py fajl paketa commerce "Inicijalizacija!" Sad kad importira sales-modul pojavljuje se tekst "Inicijalizacija" (od __init__a) ali i "Sales inicijalizacija"

# slicni mehanizam automatskog izvodjenja automatskog koda lezi u izvodjenju svakog modula koji nije main pa zbog toga da to sprijecimo u njih stavljamo kodicionalnu logiku "if name == "__main__"
# uocimo da je dovoljno jednostavno staviti npr __name__ u print da bi on kao i svaki metod dao rezultat
print("sales is initialized", __name__) # sales is initialized __main__


# dalje ide i dolazi do objasnjavanja imena __main__ i imena kojeg paket ima ako nije glavni sa kodom koji se izvodi samo ako je main!!! Sve to omogucava da se fajl koristi i kao main i kao reusable module!!!

def calculate_shipping():
    print("CSH")


def calc_tax():
    print("Tax")


if __name__ == "__main__":
    print("Sales started")  # Sales started
    calc_tax()              # Tax
