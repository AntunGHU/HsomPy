# 4'14

from pathlib import Path

path = Path("ecommerce")  # path-object koji predstavlja dir

# ? path.exists()
# ? path.mkdir()
# ? path.rmdir()
# ? path.rename("ecommerce2")

print(path.iterdir())  # <generator object Path.iterdir at 0x7fb45b56dcf0>

# posto je generator mozemož

for p in path.iterdir():
    print(p)

# i athu vraca fajlove i dirove sa pathom i rootom u ecommerce-diru

# ako imamo dir u kom nema milion filova onda mozemo konvertirati generator u LC i dobiti pathove

paths = [p for p in path.iterdir()]
print(path)

# ili

paths = [p for p in path.iterdir() if p.is_dir]
print(path)  # [PosixPath('ecom...')]

# iterdir je dobar ali ima nedostatak da nemoze traziti po npr *.py ili rekursively. Za to imamo glob()
py_files = [p for p in path.glob("**/*.py")]
print(py_files)

# za rekurivni glob
py_files = [p for p in path.rglob("**/*.py")]
print(py_files)

# bio sasm prilicno razocaran zato sto mi gotovo nista nije radilo u mojim mapama sa sustavom imena iz tecaja.py ali kad sam sve prebacio u root projekta HSOMPY sve je proradilo!!!
# dole je odziv koji je izasao kad je proradilo - trebalo bi ponoviti jednu po jednu da znamo tocno sta se gdje dobije
# ! razvrstati
# <generator object Path.iterdir at 0x7f5f8bd23c80>
# ecommerce/__init__.py
# ecommerce/customer
# ecommerce/shoping
# ecommerce/__pycache__
# ecommerce
# ecommerce
# [PosixPath('ecommerce/__init__.py'), PosixPath('ecommerce/customer/contact.py'), PosixPath('ecommerce/customer/__init__.py'), PosixPath('ecommerce/shoping/__init__.py'), PosixPath('ecommerce/shoping/sales.py')]
# [PosixPath('ecommerce/__init__.py'), PosixPath('ecommerce/customer/contact.py'), PosixPath('ecommerce/customer/__init__.py'), PosixPath('ecommerce/shoping/__init__.py'), PosixPath('ecommerce/shoping/sales.py')]
