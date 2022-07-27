# 1'57

# Uvod Atha sa pricom kako nasi programi cesto koriste druge module i resurse i kako je bitno da ih odmah i zatvore jer ako ih ne zatvore drugi koji ih budu trebali nece ih moci otvoriti!
# Ta logika u sklopu pojave gresaka dovodi do pojave da greske sprecavaju zatvaranje fajla.

try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    file.close()
except (ValueError, ZeroDivisionError):
    print("Unesi ispravan broj!")
else:
    print("No exceptions were thrown.")
print("Izvodjenje se nastavalja!")

# zato  popravak moze biti ala premjestanje close() u  except i else sto dovodi do dupliranja unosa!?
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Unesi ispravan broj!")
    file.close()
else:
    print("No exceptions were thrown.")
    file.close()
print("Izvodjenje se nastavalja!")

# rjesenje je u unosu 4. djela error-handling koda "finally" koji sada ima malo vise smisla nego kod Colt-a! Bravo Mash!
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Unesi ispravan broj!")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
print("Izvodjenje se nastavalja!")
