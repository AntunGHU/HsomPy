# 2'0

def increment(broj, za):
    return broj + za

# ? result = increment(2,1)
# ? print(result)

# ali result nije potrebno kreirati kako bi printali, moze direktno u print


print(increment(2, 1))

# ako imamo u pozivanju vise argumenata, more readable (ali i fleksibijnije jer tad mozemo manje paziti na poredak unosa argumenata) se moze postici koristenjem key-word argumenata

print(increment(broj=10, za=1))
print(increment(za=1, broj=100))
