# 3'11

# koriste se kod velikih kolicina brojeva
# kratki izlet na web sa "python3 typecode"  pretragom da se pokaze koje sve vrste objekata mozemo staviti u array: "i" - signed integer

from array import array

numbers = array("i", [1, 2, 3])

# numbers kao array tip objekta ima sve metode kao list (append, insert, pop, remove ) kao i dohvacanje sa numbers[2] isl ali svaki argument mora biti "i" kako je definiran array na pocetku! inace Error!

print(numbers)  # array('i', [1, 2, 3])
