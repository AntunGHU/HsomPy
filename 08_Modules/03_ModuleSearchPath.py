# 1'36

# ako pozivani fajl nije istoj lokaciji kao i izvodjeni, Py pretrazuje niz predefiniranih path-ova. koji su to path-ovi pokazuje nam py-modul sys

# ? import sales
import sys

# dobijemo listu pathova u kojima je 1. ithem trenutna mapa pa... niz patho-va koji ovise o OS-u
print(sys.path)

# ['d:\\za_PC\\py\\aCode\\HsomPy\\08_Modules', 'C:\\Users\\ajerkovic\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\ajerkovic\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\ajerkovic\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\ajerkovic\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\ajerkovic\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']

# na linux-u
# ['/home/antun/aCod/HsomPy/08_Modules', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages'] 