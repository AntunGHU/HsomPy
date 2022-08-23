# 3'15

from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")

# zapisivanje fajlova mape "ecommerce" u zip fajl

with ZipFile("files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)

# i zaista, uz mapu "ecommerce" pojavio se fajl "files.zip". Sad cemo ga citati

with ZipFile("files.zip") as zip:
    print(zip.namelist())

# dobije se lista: ['ecommerce/__init__.py', 'ecommerce/customer/contact.py', 'ecommerce/customer/__init__.py', 'ecommerce/customer/__pycache__/contact.cpython-310.pyc', 'ecommerce/customer/__pycache__/__init__.cpython-310.pyc', 'ecommerce/shoping/__init__.py', 'ecommerce/shoping/sales.py', 'ecommerce/shoping/__pycache__/__init__.cpython-310.pyc', 'ecommerce/shoping/__pycache__/sales.cpython-310.pyc', 'ecommerce/__pycache__/__init__.cpython-310.pyc']

# za dobiti vise informacija o bilo kom fajlu:

# ? with ZipFile("files.zip") as zip:
# ?     print(zip.namelist())
# ?     info = zip.getinfo("ecommerce/__init__.py")
# ?     print(info.file_size)
# ?     print(info.compress_size)

# ['ecommerce/__init__.py', 'ecommerce/customer/contact.py', 'ecommerce/customer/__init__.py', 'ecommerce/customer/__pycache__/contact.cpython-310.pyc', 'ecommerce/customer/__pycache__/__init__.cpython-310.pyc', 'ecommerce/shoping/__init__.py', 'ecommerce/shoping/sales.py', 'ecommerce/shoping/__pycache__/__init__.cpython-310.pyc', 'ecommerce/shoping/__pycache__/sales.cpython-310.pyc', 'ecommerce/__pycache__/__init__.cpython-310.pyc']; 0; 0

# za ekstrakciju zip-fajla u drugi - "aexctract" dir

with ZipFile("files.zip") as zip:
   print(zip.namelist())
   info = zip.getinfo("ecommerce/__init__.py")
   print(info.file_size)
   print(info.compress_size)    # 9
   zip.extractall("aextract")   # 9

# i zaista se stvorio "aexctract" dir sa sadrzajem istim kao ecommerce-dir
