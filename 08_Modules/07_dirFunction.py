# 1'39

# mocna builtin funkcija dir s kojom mozemo dobiti pregled svih metoda i propsa definiranih na nekom objektu.
# vidjeli smo da u fajlu "sales.py" nakon sto ucitamo sa
from ecommerce.shoping import sales
sales.calculate_shipping()
# dobijemo pri pozivanju i nakon tocke sve u meniju. ali nekad to ne radi kako treba pa dir radi debuganja!
print(dir(sales))
# Kontaktiran!
# CSH
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calculate_shipping', 'contact']
print(sales.__name__)  # ecommerce.shoping.sales
print(sales.__package__)  # ecommerce.shoping
# d:\za_PC\py\aCode\HsomPy\08_Modules\ecommerce\shoping\sales.py #Lin: /home/antun/aCod/HsomPy/08_Modules/ecommerce/shoping/sales.py
print(sales.__file__)
