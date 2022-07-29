"""_summary_
    """  # 3'59

# o korisnim metodama rada sa path-objektom

from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(path.stat()) # os.stat_result(st_mode=33204, st_ino=4328174, st_dev=66309, st_nlink=1, st_uid=1000, st_gid=1000, st_size=0, st_atime=1659031245, st_mtime=1659031245, st_ctime=1659031245)
# print(ctime(path.stat().st_ctime))  # Thu Jul 28 20:00:45 2022
#
# print(path.read_text())  # istice ga kao prednost pred "with open..." uz
# path.write_bytes()
# path.write_text("moj tekst")

# iako dobar za navedeno mana path-objekta pri copy koji bi isao ala
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

# target.write_text(source.read_text())

# ali ima bolji nacin sa shutil kojeg prethodno importamo pa
shutil.copy(source, target)
