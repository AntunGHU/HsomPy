# 3'28

# korisne k-de za managing dependencija, sve se kucaju u term neaktiviranog venv-a

# ? pipenv graph
# daje listu svih instaliranih dependencija
# ? requests==2.28.1
# ?  - certifi [required: >=2017.4.17, installed: 2022.6.15]
# ?  - charset-normalizer [required: >=2,<3, installed: 2.1.0]
# ?  - idna [required: >=2.5,<4, installed: 3.3]
# ?  - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.11]

# posto se u izvjescu prethodne k-de pojavljuju razlike required i installed idemo requsets deinstalirati kdom
# ? >antun@ub:~/aCod/HsomPy$ pipenv uninstall requests
# ? Uninstalling requests...
# ? Found existing installation: requests 2.28.1
# ? Uninstalling requests-2.28.1:
# ?   Successfully uninstalled requests-2.28.1
# ? 
# ? Removing requests from Pipfile...
# ? Locking [dev-packages] dependencies...
# ? Locking [packages] dependencies...
# ? Updated Pipfile.lock (16c839)!

# request je otisao sto mozemo vidjeti i u Pipfajl-u u kom ga vise nema a ni u sklopu kde pipenv graph ga vise nema 
# ? > pipenv graph
# ? certifi==2022.6.15
# ? charset-normalizer==2.1.0
# ? idna==3.3
# ? urllib3==1.26.11
# ali dipendencije requests-a su ostale!!!
# medjutim, ako bi mi sada svoj kod prebacili na drugi server i instalirali sve ove dependencije od nule, ove dependencije nebi tamo dosle jer nemamo referncija na njih u nasem pipfile-u.
# zato instaliramo raniju verziju requests-a
# ? > pipenv install requests==2.9.* 
# i time pravimo unos u nas pipfile
# ? antun@ub:~/aCod/HsomPy$ pipenv install requests==2.9.*
# ? Installing requests==2.9.*...
# ? Adding requests to Pipfile's [packages]...
# ? ✔ Installation Succeeded 
# ? Pipfile.lock (16c839) out of date, updating to (3d6cc6)...
# ? Locking [dev-packages] dependencies...
# ? Locking [packages] dependencies...
# ? Building requirements...
# ? Resolving dependencies...
# ? ✔ Success! 
# ? Updated Pipfile.lock (3d6cc6)!
# ? Installing dependencies from Pipfile.lock (3d6cc6)...
# ?   🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
# ? To activate this project's virtualenv, run pipenv shell.
# ? Alternatively, run a command inside the virtualenv with pipenv run.

# za naci i updejtati outdated packages:
# ? > pipenv update --outdated
# ? antun@ub:~/aCod/HsomPy$ pipenv update --outdated
# ? Building requirements...
# ? Resolving dependencies...
# ? ✔ Success! 
# ? Skipped Update of Package requests: 2.9.2 installed, 2.9.2 required (==2.9.# ? * set in Pipfile), 2.28.1 available.
# ? All packages are up to date!
# upozorenje "Skipped..." kaze da nije instalirao najnoviji paket (kojem bi se minor ili major verzija razlikovale od trenutne verzija koja je imala * samo na pach-grupi tj 2.9.*
# Ako odemo u Pipfile i rucno stavimo * na drugu brojku tj 2.* i ponovimo ko-du:
# ? > pipenv update --outdated
# i kod njega se vise zuto upozorenje ne pojavljuje ali i dalje kaze da je request out-of-date.
# sad imamo 2 mogucnosti, updejtati sve pakete ili samo odredjeni pa to radimo sa:
# ? > pipenv update requests
# ? Locking [dev-packages] dependencies...
# ? Locking [packages] dependencies...
# ? Building requirements...
# ? Resolving dependencies...
# ? ✔ Success! 
# ? Updated Pipfile.lock (cafc10)!
# ? Installing dependencies from Pipfile.lock (cafc10)...
# ?   🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/1 — 00:00:00
# ? To activate this project's virtualenv, run pipenv shell.
# ? Alternatively, run a command inside the virtualenv with pipenv run.
# ? All dependencies are now up-to-date!
# ako sad pogledamo pipfile.lock vidit cemo da je requests 2.28.1
# a to ce pokazati i 
# ? > pipenv graph
# ? requests==2.28.1
# ?   - certifi [required: >=2017.4.17, installed: 2022.6.15]
# ?   - charset-normalizer [required: >=2,<3, installed: 2.1.0]
# ?   - idna [required: >=2.5,<4, installed: 3.3]
# ?   - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.11]