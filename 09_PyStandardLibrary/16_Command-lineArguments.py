# 1'54

# ili kako kroz py-fajl dobaciti nove argse za term

# pocinjemo sa izvodjenjem nase skripte u termu dajuci k-du python3 app.py -a -b -c na sto sam dobio ['app.py', '-a', '-b', '-c']
# potom u isti app.py ubacujem donji import i print i dobija Ath isti odziv ['app.py', '-a', '-b', '-c'] ali ja ne nego vidi dole!

# ? > python3 app.py -a -b -c  # ['app.py', '-a', '-b', '-c']

import sys

from click import password_option

print(sys.argv)  # ['/home/antun/aCod/HsomPy/app.py']

# posebni argumenti u Ath-a pruzaju mogucnosti:

if len(sys.argv) == 1:  # situacija kad user nije dao dodatne argse
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)

# sad kad se ovaj "app.py" pozove iz terma s komandom "python3 app.py" (dakle bez dodatnih parametara) dobijemo samo "USAGE: python3 app.py <password>" a ako pokrenemo app.py sa bilo kojim parametrima npr "python3 app.py 1234"  u termu izlazi "Password 1234"
