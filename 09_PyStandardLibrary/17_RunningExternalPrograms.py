# 8'06
# dakle, kako cemo iz .py pokretati eksterne programe.async Stvar korisna pri automatizaciji.
# recimo, zelimo iz py-fajla pokrenuti "ls" i hvatati output. Modul subprocess sa svojim metodama!!!

import subprocess

# ? subprocess.call
# ? subprocess.check_call
# ? subprocess.check_output

# svi ovi metodi su helpers-metodi za stvaranje "Popen" klase. Dok se gornji sada slabije koriste i vise se smatraju kao "legacy" za stvaranje Popen - klase posebno se koristi run() metod! 
# subprocess.Popen # Popen - process open

# ? completed = subprocess.run(["ls", "-l"]) #
# ? total 940
# ? drwxrwxr-x 2 antun antun   4096 srp  24 07:55 01_GettingStarted
# ? drwxrwxr-x 2 antun antun   4096 srp  24 08:06 02_PrimitiveTypes
# ? drwxrwxr-x 2 antun antun   4096 srp  19 07:33 03_ControlFlow
# dakle, radi!

# ? print(type(completed))# <class 'subprocess.CompletedProcess'>

# completed object ima puno atributa (args, stderr, stdout) itd

# ? print("args", completed.args)   # args ['ls', '-l'] # pokazuje k-de koje radimo
# ? print("returncode", completed.returncode)   # returncode 0 # 0-uspjeh, 1-bljak
# ? print("stderr", completed.stderr)   # stderr None # logicno jer je gore 0
# ? print("stdout", completed.stdout)   # stdout None # jer ne hvatamo "capturamo" nego ide direktno vani

# ako bi htjeli hvatati output on ce ici na stdout ali nece biti na terminalu!
# ? completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# ? print("args", completed.args) 
# ? print("returncode", completed.returncode) 
# ? print("stderr", completed.stderr)
# ? print("stdout", completed.stdout) 
# args ['ls', '-l']; returncode 0; stderr b''

# i dobijemo izlaze i nista na treminalu ali ako odkomentiramo stdout
# ? print("stdout", completed.stdout)
# stdout b'total 940\ndrwxrwxr-x 2 antun antun   4096 srp  24 07:55 01_GettingStarted\ndrwxrwxr-x 2 antun antun   4096 srp  24 08:06 02_PrimitiveTypes\ndrwxrwxr-x 2 antun ant11_PopularPyPackages\ndrwxrwxr-x 2 antun antun   4096 srp   6 04:56 12_BuildingWebAppsWithDjango\ndrwxrwxr-x 2 antun antun   4096 srp   6 04:56 13_MachineLearningWithPy\ndrwxrwxr-x 3 antun antun   4096 srp  29 08:00 aextract\n-rw-rw-r-- 1 antun antun   1730 srp  30 10:15 app.py\n-rw-rw-r-- 1 antun antun 860701 srp  12 16:32 beauty.png\n-rw-rw-r-- 1 antun antun     51 srp  29 08:22 data.csv\n-rw-rw-r-- 1 antun antun  12288 srp  29 16:07 db.sqlite3\ndrwxrwxr-x 5 antun antun   4096 srp  28 20:00 ecommerce\n-rw-rw-r-- 1 antun antun   3005 srp  29 07:48 files.zip\n-rw-rw-r-- 1 antun antun      0 srp  28 21:02 __init__.py\n-rw-rw-r-- 1 antun antun    102 srp  29 16:07 movies.json\ndrwxrwxr-x 2 antun antun   4096 srp  28 20:00 __pycache__\n-rw-rw-r-- 1 antun antun    128 srp  30 07:43 template.html\n'

# obratimo paznju da izlazu prethodi "b" tj oznaka binarnosti. Konvertiranje u string dodavanjem jos jednog argumenta "text=True" poslije cega stdout postaje regular-string-object
# ? drwxrwxr-x 2 antun antun   4096 srp  24 07:55 01_GettingStarted
# ? drwxrwxr-x 2 antun antun   4096 srp  24 08:06 02_PrimitiveTypes
# ? drwxrwxr-x 2 antun antun   4096 srp  19 07:33 03_ControlFlow
# ? drwxrwxr-x 3 antun antun   4096 srp  29 08:00 aextract
# ? -rw-rw-r-- 1 antun antun   3423 srp  30 10:20 app.py
# ? -rw-rw-r-- 1 antun antun 860701 srp  12 16:32 beauty.png
# ? -rw-rw-r-- 1 antun antun     51 srp  29 08:22 data.csv
# ? -rw-rw-r-- 1 antun antun  12288 srp  29 16:07 db.sqlite3
# ? drwxrwxr-x 5 antun antun   4096 srp  28 20:00 ecommerce
# ? -rw-rw-r-- 1 antun antun   3005 srp  29 07:48 files.zip
# ? -rw-rw-r-- 1 antun antun      0 srp  28 21:02 __init__.py
# ? -rw-rw-r-- 1 antun antun    102 srp  29 16:07 movies.json
# ? drwxrwxr-x 2 antun antun   4096 srp  28 20:00 __pycache__
# ? -rw-rw-r-- 1 antun antun    128 srp  30 07:43 template.html

# u nastavku Ath primjer za subprocess prosiruje sa stvaranjem dodatnog fajla "other.py" u root-u projekta
# sad se taj fajl izvodi tako da se stavi u subprocess

# ? completed = subprocess.run(["python3", "other.py"], capture_output=True, # ? text=True)
# ? print("args", completed.args) # args ['python3', 'other.py']
# ? print("returncode", completed.returncode) # returncode 0
# ? print("stderr", completed.stderr) # stderr 
# ? print("stdout", completed.stdout) # stdout Here is complicated script!

# napominje da su scripta app.py i other.py dva razlicita procesa i svaki se odvija u svom memory-prostoru, nece djeliti iste varijable

# za kraj Ath pokazuje returnkod 1 pomocu 
# ? completed = subprocess.run(["false"], capture_output=True, text=True, # ? check=True)
# ? print("args", completed.args) # args ['false']
# ? print("returncode", completed.returncode) # returncode 1
# ? print("stderr", completed.stderr) # stderr 
# ? print("stdout", completed.stdout) # stdout

# Ako se to desi jedan pristup bi bio
# ? if completed.returncode != 0:
# ?     print(completed.stderr)
    
# drugi pristup bi bio dodavanje jos jednog keyarga "check=True" nakon cega dobijamo:
# ? subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.
# imajuci ovu gresku mozemo maknuti if blok i ubaciti try-blok
try:
    completed = subprocess.run(["false"], capture_output=True, text=True,  check=True)
    print("args", completed.args) # args ['false']
    print("returncode", completed.returncode) # returncode 1
    print("stderr", completed.stderr) # stderr 
    print("stdout", completed.stdout) # stdout
except subprocess.CalledProcessError as ex:
    print(ex)

