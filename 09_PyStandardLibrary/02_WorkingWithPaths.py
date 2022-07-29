# 4'48

# Oko rada s files and dirs
# Centralna tema "Path" jer to je osnova rada s files and dirs

from pathlib import Path

# ? Path(r"C:\Program Files\Microsoft")
# ? Path("/usr/local/bin")
# ? Path()
path = Path("ecommerce/__init__.py")
# ? Path() / "ecommerce" / "__init__.py"
# ? Path.home()

# path-objekt ima prilicno korisnih clanova a mi cemo neke, za vise googlati sa "python 3 pathlib" i na stranicu https://docs.python.org/3/library/pathlib.html gdje mozemo vidjeti sve clanove Path-klase

path.exists()  # da vidimo dali fajl ili dir postoji
path.is_file()  # dali je file
path.is_dir()  # dir?

print(path.name)  # __init__.py  # returna fajl-name u ovom path-u
print(path.stem)  # __init__ # ime fajla bez ekstenzije
print(path.suffix)  # .py # ime fajl-ekstenzije
print(path.parent)  # ecommerce

path = path.with_name("file.txt")
print(path)  # ecommerce/file.txt
print(path.absolute())  # /home/antun/aCod/HsomPy/ecommerce/file.txt

path = path.with_suffix(".txt")
print(path)  # ecommerce/file.txt
