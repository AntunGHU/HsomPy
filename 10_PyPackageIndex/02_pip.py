# 6'23

# za instaliranje
# ? > pip3 install requests
# ako trazi update
# ? > pip3 install --upgrade pip
# za vidjeti sto je trenutno instalirano
# ? > pip3 list
# 1.brojka MajorVer, 2.MinVer, #.Patch
# primjer s requests i biranje bez 2 ili 3

# za install tocno zeljene verzije a ne zadnje
# ? > pip3 install requests==2.9.0
# ili uz *
# ? > pip3 install requests==2.9.*
# ako se pojavi poruka da vec je onda moramo prvo deinstalirati
# ? > pip3 uninstall requests
# pa onda instaliramo sa * ili sa malo varijacijom
# ? > pip3 install requests~=2.9.0

# asterix mozemo i za 2. brojku koristiti
# ? > pip3 install requests==2.*

# nakon pip-instalacije paket dalje koristimo kao i one iz py-standard-lib tj importanje itd
import requests
requests.api  # i gomila drugih metoda itd a sto je to itd vidimo na dnu stranice o requests paketu gdje se nalazi link na dokumentaciju!!!
