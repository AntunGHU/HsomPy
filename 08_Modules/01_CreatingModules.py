# 4'16

# moduli su dijelovi koda smjesteni u zasebne fajlove-module. Imena im dajemo po pravilima varijabli (mala slova a za viserijecne nazive fajlova snake case)
# ako trebamo pozvati kod (povezati taj kod sa kodom main fajla) cinimo to upotrebom sintakse "from ime_fajla_bez_ekstenzije import ime_funkcije". Naravno, intelisence ce pokazati sta sve imamo u tom fajlu. Npr

import sales
from sales import calculate_shipping

calculate_shipping()

# imefajla ide samo ako je u istom dir-u kao i fajl koji ga poziva, inace se mora napisati apsolutni path
# ako zelimo importati vise funkcija u jednom from-u koristimo zarez
# koristenje * radi importa svega je bad pactice jer se mogu pojaviti istoimene funkcije i sl koji ce onda overwritten istoimene u nasem main fajlu!
# drugi nacin importa (import sales) rezultira da je pozivanje sa imenom modula

sales.calculate_shipping()
