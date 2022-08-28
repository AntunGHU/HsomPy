# 8'06

# kako cemo iz .py scripti pokretati eksterne programe - stvar korisna pri automatizaciji.
# recimo, zelimo iz py-fajla pokrenuti "ls" i hvatati output. Modul subprocess sa svojim metodama!!!
# ovdje sam prvi put poceo obracati paznju na detalje iskocnih informacija intelisensa: kockice-metodi, plave[]-atributi, kljuc-?
# u njegovom prikazu ima 4 vrste a kao i u najnovijem neki su sa * pokraj a neki ne!

import subprocess

# prije su se cesto koristili
# ? subprocess.call
# ? subprocess.check_call
# ? subprocess.check_output 
# na gornje ne treba vise trositi vrijeme!
# svi ovi su ala "legacy"-helper i nisu vise najbolji izbor.  

# Nowdays se posebno preferira # * run()-metod za stvaranje Popen - klase.
completed = subprocess.run(["ls", "-l"]) #
#* i izlaz terminala pun!!! dakle, radi! run ima dosta keyword - defaultnih argumenata


completed =subprocess.run(["ls", "-l"])  # completed ima puno metoda i atributa a najvazniji atributi su:
print("args", completed.args)               # args ['ls', '-l']         # pokazuje k-de koje radimo
print("returncode", completed.returncode)   # returncode 0              # 0-uspjeh, 1-bljak
print("stderr", completed.stderr)           # stderr None               # logicno jer je gore 0 inace bi bila error-poruka
print("stdout", completed.stdout)           # stdout None               # jer ne hvatamo "capturamo" nego ide direktno vani

# ako pozelimo izlaz save-ati u fajl koristimo def-arg od run-a "capture_output=True"
completed =subprocess.run(["ls", "-l"], capture_output=True)
print("args", completed.args)               # args ['ls', '-l']         
print("returncode", completed.returncode)   # returncode 0              
print("stderr", completed.stderr)           # stderr b''             
print("stdout", completed.stdout)           #? stdout b'total 1084\ndrwxrwxr-x 2 antun antun   4096 srp  24 07:55 01_GettingStarted\ndrwxrwxr-x 2 antun antun   4096 srp  24 08:06 02_PrimitiveTypes\ndrwxrwxr-x 2 antun antun   4096 kol  14 13:32 03_ControlFlow\ndrwxrwxr-x 2 antun antun   4096 kol  14 13:50 04_Functions\ndrwxrwxr-x 2 antun antun   4096 kol  10 04:05 05_DataStructures\ndrwxrwxr-x 2 antun antun   4096 kol  10 11:32 06_Exceptions\ndrwxrwxr-x 2 antun antun   4096 kol  22 10:18 07_Classes\ndrwxrwxr-x 4 antun antun   4096 kol  22 18:43 08_Modules\ndrwxrwxr-x 2 antun antun   4096 kol  27 06:42 09_PyStandardLibrary\ndrwxrwxr-x 2 antun antun   4096 kol  13 18:29 10_PyPackageIndex\ndrwxrwxr-x 2 antun antun   4096 srp  31 11:50 11_PopularPyPackages\ndrwxrwxr-x 2 antun antun   4096 srp  31 13:40 12_BuildingWebAppsWithDjango\ndrwxrwxr-x 2 antun antun   4096 srp  31 19:15 13_MachineLearningWithPy\ndrwxrwxr-x 3 antun antun   4096 srp  29 08:00 aextract\n-rw-rw-r-- 1 antun antun     78 srp  30 16:56 app.py\n-rw-rw-r-- 1 antun antun 860701 srp  12 16:32 beauty.png\n-rw-rw-r-- 1 antun antun      0 srp  31 07:24 config.py\n-rw-rw-r-- 1 antun antun     51 kol  23 10:47 data.csv\n-rw-rw-r-- 1 antun antun  12288 srp  29 16:07 db.sqlite3\ndrwxrwxr-x 5 antun antun   4096 kol  23 08:36 ecommerce\n-rw-rw-r-- 1 antun antun   3014 kol  23 10:39 files.zip\n-rw-rw-r-- 1 antun antun      9 kol  23 09:16 __init__.py\n-rw-rw-r-- 1 antun antun    102 srp  29 16:07 movies.json\n-rw-rw-r-- 1 antun antun     36 srp  30 10:30 other.py\ndrwxrwxr-x 2 antun antun   4096 srp  28 20:00 __pycache__\n-rw-rw-r-- 1 antun antun    128 srp  30 07:43 template.html\n-rw-rw-r-- 1 antun antun 132090 srp  31 06:56 Yelp.png\n-rw-rw-r-- 1 antun antun    181 srp  31 07:23 yelp.txt\n'
#* i izlaz se vise ne daje na ekran nego preko atributa stdout ali koji u ovakvoj kdi daje "b"-binary output! da bi bilo u tekstu treba k-di run dodati drugi keyword atg "text=True"

completed =subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("args", completed.args)               # args ['ls', '-l']         
print("returncode", completed.returncode)   # returncode 0              
print("stderr", completed.stderr)           # stderr            
print("stdout", completed.stdout)           # stdout total 1084
#? drwxrwxr-x 2 antun antun   4096 srp  24 07:55 01_GettingStarted
#? drwxrwxr-x 2 antun antun   4096 srp  24 08:06 02_PrimitiveTypes
#? drwxrwxr-x 2 antun antun   4096 kol  14 13:32 03_ControlFlow
#? drwxrwxr-x 2 antun antun   4096 kol  14 13:50 04_Functions
#? drwxrwxr-x 2 antun antun   4096 kol  10 04:05 05_DataStructures
#? drwxrwxr-x 2 antun antun   4096 kol  10 11:32 06_Exceptions
#? drwxrwxr-x 2 antun antun   4096 kol  22 10:18 07_Classes
#? drwxrwxr-x 4 antun antun   4096 kol  22 18:43 08_Modules
#? drwxrwxr-x 2 antun antun   4096 kol  27 06:47 09_PyStandardLibrary
#? drwxrwxr-x 2 antun antun   4096 kol  13 18:29 10_PyPackageIndex
#? drwxrwxr-x 2 antun antun   4096 srp  31 11:50 11_PopularPyPackages
#? drwxrwxr-x 2 antun antun   4096 srp  31 13:40 12_BuildingWebAppsWithDjango
#? drwxrwxr-x 2 antun antun   4096 srp  31 19:15 13_MachineLearningWithPy
#? drwxrwxr-x 3 antun antun   4096 srp  29 08:00 aextract
#? -rw-rw-r-- 1 antun antun     78 srp  30 16:56 app.py
#? -rw-rw-r-- 1 antun antun 860701 srp  12 16:32 beauty.png
#? -rw-rw-r-- 1 antun antun      0 srp  31 07:24 config.py
#? -rw-rw-r-- 1 antun antun     51 kol  23 10:47 data.csv
#? -rw-rw-r-- 1 antun antun  12288 srp  29 16:07 db.sqlite3
#? drwxrwxr-x 5 antun antun   4096 kol  23 08:36 ecommerce
#? -rw-rw-r-- 1 antun antun   3014 kol  23 10:39 files.zip
#? -rw-rw-r-- 1 antun antun      9 kol  23 09:16 __init__.py
#? -rw-rw-r-- 1 antun antun    102 srp  29 16:07 movies.json
#? -rw-rw-r-- 1 antun antun     36 srp  30 10:30 other.py
#? drwxrwxr-x 2 antun antun   4096 srp  28 20:00 __pycache__
#? -rw-rw-r-- 1 antun antun    128 srp  30 07:43 template.html
#? -rw-rw-r-- 1 antun antun 132090 srp  31 06:56 Yelp.png
#? -rw-rw-r-- 1 antun antun    181 srp  31 07:23 yelp.txt
# * i sad smo dobili regularni text izlaz kojeg mozemo printati na terminal ili save-ati u fajl!

# a sad kako pokrenuti drugu skriptu ili program
completed =subprocess.run(["python3", "other.py"], capture_output=True, text=True)
print("args", completed.args)               # args ['python3', 'other.py']        
print("returncode", completed.returncode)   # returncode 0              
print("stderr", completed.stderr)           # stderr            
print("stdout", completed.stdout)           # stdout Here is complicated script!
#* i other (u root-u prompta) je pokrenut, args-i su oni iz [], stdout je sadrzaj other-fajla! Na ovaj nacin skripta other.py bit ce izvedena kao child proces i bit ce u potpuno drugom memorijskom prostoru sto je drugacije nego da sam je importao a appp.py. appp.py i other.py bit ce odvojeni procesi i nece dijeliti iste varijable!

# i za kraj kad nije 0 tj kad imamo error! sto cemo simulirati komandom "false"
completed =subprocess.run(["false"], capture_output=True, text=True)
print("args", completed.args)               # args ['false']   
print("returncode", completed.returncode)   # returncode 1              
print("stderr", completed.stderr)           # stderr            
print("stdout", completed.stdout)           # stdout
#* i izlaz je greska a provjeru mozemo sa dodavanjem if i jos jednog keyarga "check=True" ala kad se reisa error

#? completed =subprocess.run(["false"], capture_output=True, text=True, check=True)
#? print("args", completed.args)               # args ['false']   
#? print("returncode", completed.returncode)   # returncode 1              
#? print("stderr", completed.stderr)           # stderr            
#? print("stdout", completed.stdout)           # stdout
#? #* i izlaz je greska a provjeru mozemo sa ala 
#? if completed.returncode != 0:
#?     print(completed.stderr) # subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.
    
# drugi pristup bi bio s try kad nam if vise ne treba ali program goes on!:
try:
    completed = subprocess.run(["false"], capture_output=True, text=True,  check=True)
    print("args", completed.args)               # preskocen
    print("returncode", completed.returncode)   # preskocen
    print("stderr", completed.stderr)           # preskocen 
    print("stdout", completed.stdout)           # preskocen
except subprocess.CalledProcessError as ex:
    print(ex)  # ? subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.