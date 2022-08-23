# 4'48

# Oko rada s files and dirs
# Centralna tema "Path" jer to je osnova rada s files and dirs

from pathlib import Path

# razne kombinacije pri kreiranju Path objekata:
# apsolute path
# ? Path(r"C:\Program Files\Microsoft")
# ? Path("/usr/local/bin")
# path koji predstavlja trenutni folder
# ? Path()
# trenutni folder sa subfolderom "ecommerce"
path = Path("ecommerce/__init__.py") #* Path objekt kojeg koristimo dalje u ovom demou!
# kombiniranje vise Path-objekata pomocu / i drugog Pathobjekta
# ? Path() / Path("ecommerce") / 
# kombiniranje vise Path-objekata pomocu / i stringa
# ? Path() / "ecommerce" / "__init__.py"
# Path home-dira
# ? Path.home()

# path-objekt ima prilicno mnogo korisnih clanova a mi cemo neke, za vise googlati sa "python 3 pathlib" i na stranicu https://docs.python.org/3/library/pathlib.html gdje mozemo vidjeti sve clanove Path-klase

print(path.exists())  # da vidimo dali fajl ili dir postoji     # True
print(path.is_file())  # dali je file   # True
print(path.is_dir())  # dir?    # False

print(path.name)  # __init__.py  # returna fajl-name u ovom path-u
print(path.stem)  # __init__ # ime fajla bez ekstenzije
print(path.suffix)  # .py # ime fajl-ekstenzije
print(path.parent)  # ecommerce

path1 = path.with_name("file.txt") #* izmjena objekta path
print(path1)  # ecommerce/file.txt
print(path1.absolute())  # /home/antun/aCod/HsomPy/ecommerce/file.txt

path2 = path.with_suffix(".txt")
print(path2)  # ecommerce/__init__.txt  # stvarno nismo preimenovali ekstenziju nego samo path-objekt
