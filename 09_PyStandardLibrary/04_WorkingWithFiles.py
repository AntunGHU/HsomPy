# 3'59

# o korisnim metodama rada sa path-objektom

from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py") # objekt koji predstavlja samo "__init__.py" fajl
print(path.exists())    # True
# ? print(path.rename("init.txt")) # init.txt # primenuje i stavlja u radni dir!
# ? path.unlink() # brise fajl


print(path.stat()) 
# i dobijemo malo statistike, za ovo nam nije trebao ctime-modul
#? os.stat_result(st_mode=33204, st_ino=4328174, st_dev=66309, st_nlink=1, st_uid=1000, st_gid=1000, st_size=0, st_atime=1659031245 (acces time), st_mtime=1659031245 (modification time), st_ctime=1659031245 (creation time pocevsi od starttime, na unix-ima start time je 1.1.1970))

# ako hocemo human-readable importamo ctime-modul i file-objekt ubacimo kao argument u ctime-funkciju
print(ctime(path.stat().st_ctime))  
# ? Thu Jul 28 20:00:45 2022

# imamo i nekoliko metoda za citanje podataka from the file
print(path.read_bytes())    # ? b'print("tekst")' 
# metodi za string-citanje # istice ga kao prednost pred "with open..." uz uzimanje svih nj osobina!
print(path.read_text())     # ? "print("tekst")" 

# imamo i za pisanje, kao i with otvara i zatvara fajl
# ? path.write_bytes("10101010") #? TypeError: memoryview: a bytes-like object is required, not 'str'
path.write_text("moj tekst") # pise u w-modu tj prepisuje

# iako dobar za navedeno (read, write) mana je path-objekta pri copy
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py" # dakle kopirat cemo ga u trenutni dir kao fajl imena navedenog
target.write_text(source.read_text()) # i odradjeno, tekst je sada i u korijenskom init-u

# ali ima bolji nacin sa shutil kojeg prethodno importamo pa
shutil.copy(source, target)
