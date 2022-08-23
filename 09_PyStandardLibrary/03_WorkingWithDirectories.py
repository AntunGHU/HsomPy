# 4'14

from pathlib import Path

path = Path("ecommerce")  # path-object koji predstavlja dir "ecommerce"

#? print(path.exists()) # True
#? print(path.mkdir())  # FileExistsError: [Errno 17] File exists: 'ecommerce'
#? print(path.rmdir())  # OSError: [Errno 39] Directory not empty: 'ecommerce'
#? print(path.rename("ecommerce2"))   # ecommerce2 

print(path.iterdir())  # <generator object Path.iterdir at 0x7fb45b56dcf0>

# posto je generator mozemo

for p in path.iterdir():
    print(p)

# i dobijemo sadrzaj ecommerce dira, i subdire i fajlove!
#? ecommerce/__init__.py
#? ecommerce/customer
#? ecommerce/shoping
#? ecommerce/__pycache__

# ili ako u diru nemamo milion dirova ili fajlova (kad je upotreba generatora logicnija kao gore) mozemo koristiti LC
paths = [p for p in path.iterdir()]
print(paths)    
# i dobijemo (na Lx) listu Posix pathova, da smo na Win-u dobili bi drugacije!
# ? [PosixPath('ecommerce/__init__.py'), PosixPath('ecommerce/customer'), PosixPath('ecommerce/shoping'), PosixPath('ecommerce/__pycache__')]

# pokusaj malog filtriranja
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
# i dobijemo isti spisak bez fajla, samo dir-evi
# ? [PosixPath('ecommerce/customer'), PosixPath('ecommerce/shoping'), PosixPath('ecommerce/__pycache__')]

# iterdir je dobar ali ima nedostatak da nemoze traziti po npr *.py ili rekursively. Za to imamo glob()
py_files = [p for p in path.glob("*.py")]
print(py_files)
# i dobijemo sve fajlove sa .py ekstenzijom u dir-u 
# ? [PosixPath('ecommerce/__init__.py')]


# za rekursivly glob
py_files = [p for p in path.glob("**/*.py")]
print(py_files)
# i dobijemo sve fajlove sa .py ekstenzijom u dir-u i njegovim poddirevima (to je znacenje recursively!!!)
# ? [PosixPath('ecommerce/__init__.py'), PosixPath('ecommerce/customer/contact.py'), PosixPath('ecommerce/customer/__init__.py'), PosixPath('ecommerce/shoping/__init__.py'), PosixPath('ecommerce/shoping/sales.py')]


# ili sa "rglob"
# za rekursivly glob
py_files = [p for p in path.rglob("*.py")]
print(py_files)
# i dobijemo sve fajlove sa .py ekstenzijom u dir-u i njegovim poddirevima
# ? [PosixPath('ecommerce/__init__.py'), PosixPath('ecommerce/customer/contact.py'), PosixPath('ecommerce/customer/__init__.py'), PosixPath('ecommerce/shoping/__init__.py'), PosixPath('ecommerce/shoping/sales.py')]