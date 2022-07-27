# 4'10

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Unesi broj!")
    print(ex)   # invalid literal for int() with base 10: 'a'
    print(type(ex))  # <class 'ValueError'>
else:
    print("No exceptions were thrown.")
print("Izvodjenje se nastavalja!")
