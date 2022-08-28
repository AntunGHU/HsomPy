# 3'49

# code runner run-a scripte sa global py-interpreterom a ne od pipenv-a - tako bilo 2018 a tako je i danas!!! 
# coderunner poteze global-pyinterpreter, otvara drugi bashshell u termu a vec aktivirani venv ne kuzi!
# za koristenje py-interpretera od pipenv-a moramo pokrenuti k-du unutar aktiviranog venv-termapipenv 
# ? HsomPyantun@ub:~/aCod/HsomPy$ python3 10_PyPackageIndex/05_VirtualEnvironmentsInVSCode.py 
# i dobijamo odgovor
# ? <Response [200]>

import requests

response = requests.get("http://google.com")

print(response) # # ? <Response [200]>

# da bi to popravili trebamo reci coderunner-u koji intrepreter koristiti. U tu svrhu prvo sa 
# ? HsomPyantun@ub:~/aCod/HsomPy$ pipenv --venv
# nalazimo Path do naseg venv-a  kad dobijemo odgovor
# ? /home/antun/.local/share/virtualenvs/HsomPy-tyO_AMhm

# sad Ath pokazuje dolazak do te mape a ja idem preko klika na verziju py-a u status baru i dolazim do browse za path i nalazim py-interpreter od pipenv-a te nakon odabira uspjevam sa kodrunerom  i pipenv-intrepreterom pokrenuti svoju skriptu doduse uz otvaranje ponovno jos jednog shela (to je automatizam coderunnera napravljen za slucaj kad terminal nije otvoren). u svakom slucaju uspio sam da koderunner ostaje unutar pipenv-a i sa njegovim interpreterom.

# no posto je ovo ponasanje kratke pameti (valjda je tako onda bilo, sada ni gasenje vsc-ea nece promjeniti isbrowsanog interpretera) Ath ide kroz user settingse tri tocke ... koje ja nemam i rucno upisuje u json setingse koje ja takodjer ne mogu otvoriti.

# prelazak na pipenv py-interpreter  popracen je opet ponudama o instalaciji lintera i dr. dodataka iz py-ekstenzije!