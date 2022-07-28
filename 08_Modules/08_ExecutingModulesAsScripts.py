# 2'55

# opet Ath u "sales.py" modulu u kom imamo 2 funkcije
# ali mozemo imati i bilo koji statement koji ce biti izvrsen prvi puta kad se modul ucitava!
# kao primjer daje liniju "print("Sales initialized")"
# ako sada izvedemo fajl npr app.py-a u kojem je sales importan, taj dio se pojavljuje na output-u!! tj sales je inicijaliziran!!
# koristeci isti nacin mozemo tako inicijalizirati nase pakete
# ath ide sa csp u komand-paletu i kuca  u __init__.py fajl paketa commerce "Inicijalizacija!"
# dalje ide i dolazi do objasnjavanja imena __main__ i imena kojeg paket ima ako nije glavni sa kodom koji se izvodi samo ako je main!!!

if __name__ == "__main__":
    print("Sales started")
    calc_tax()
