# 3'05

# primjer sa novom vrstom greske i ponovnim krasanjem!
try:
    age = int(input("Age: "))
    xfactor = 10 / age  # ZeroDivisionError: division by zero
except ValueError:
    print("Unesi broj!")
else:
    print("No exceptions were thrown.")
print("Izvodjenje se nastavalja!")


# rjesenje moze biti u uvodjenju novog exception-a
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("Unesi broj!")
except ZeroDivisionError:
    print("Age nemoze biti nula!")
else:
    print("No exceptions were thrown.")
print("Izvodjenje se nastavalja!")

# ili objedinjavanjem u jedan excetion
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Unesi ispravan broj!")
else:
    print("No exceptions were thrown.")
print("Izvodjenje se nastavalja!")
