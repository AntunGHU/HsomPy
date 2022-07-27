# 3'07

# Ovdje je Ath mislio kako je pravo mjesto da i nastavi sa openima fajlova te je predstavio "with" koji je finally ucinio nepotrebnim!

try:
    with open("app.py") as file:
        print("File opened!")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Unesi ispravan broj!")
else:
    print("No exceptions were thrown.")
print("Izvodjenje se nastavalja!")

# kao Mashovstine malo dodao je i mogucnost jos jednog open-ovanja za jedan with i malo spominjao osobine class-e i dundere __enter__ i __exit__

try:
    with open("app.py") as file, open(drugifajl.txt) as target:
        print("File opened!")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Unesi ispravan broj!")
else:
    print("No exceptions were thrown.")
print("Izvodjenje se nastavalja!")
