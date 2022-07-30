# 4'48

# instalacija pipenv-a tj bilo kakvog paketa komandom pipenv, ostavlja u root-u projekta Pipfile i Pipfile.lock koji su namjenjeni pracenju dependencija u projektima.
# otvaranjem Pipfile-a vidimo odjeljke [source](s koje se adrese paket instalirao), [dev-packages](paketi za deployment i testiranja), [packages](ima samo requests sa = * koji je rezultata instalacije bez specificiranja verzije pa oznacava latest) i [requires](specificira python_version = "3.9" potrebnu za run-anje ove app)
# Pipfile.lock je json fajl koji pokazuje dependencije (u ovom slucaju od requests-a) i njihove tocne verzije!
# sa ta dva fajla mozemo uzeti nas app-cod i reproducirati execution environment na serveru, i time se minimizira mogucnost da app radi kod nas ali na serveru ne!
# Workflow:
# Nalazenje virtualenva sa
# ? > pipenv --venv 
# ali ne mogu izaci vise jer kad otkucam "exit" on izlazi iz terma i kad term ponovo otvorim on je automatski u nj, ipak sam zatvorivsi folder  i ponovo ulazeci uspio biti izvan venv-a i ukucavam k-du # ? > pipenv --venv 
# Ljepo mi vraca lokaciju venv-a pri cemu prompt jos uvjek ostaje izvan: #? /home/antun/.local/share/virtualenvs/HsomPy-tyO_AMhm
# sad ce Ath simulirati prebacivanje naseg projekta na server na kome nema venv-a, dakle samo source-cod nase aplikacije. To radi tako da brise ovaj direktorije venv-a kdom:
# ? > rm -rf /home/antun/.local/share/virtualenvs/HsomPy-tyO_AMhm
# i kad provjerim sa # ? > pipenv --venv 
# dobijem: #? No virtualenv has been created for this project(/home/antun/aCod/HsomPy) yet!
# ? Aborted!
# znaci sve sto nam je ostalo je sourcekod i pipfile-si koji trackaju nase dependencije!
# kad dodjemo na novi server i lociramo se kursorom tj termom u root nase aplikacije-projekta otkucamo 
# ? > pipenv install
# sljedi postupak instalacija nakon kojeg ako ponovo provjerimo sa
# ? > pipenv --venv
# dobijemo za odgovor
# ? > /home/antun/.local/share/virtualenvs/HsomPy-tyO_AMhm
# Medjutim, instalacija po Pipfile-u je instalirala (zbog *) najnoviju verziju requests paketa a dependencije su imale neke druge brojeve. Postoji velika sansa app na novom serveru ne radi! Da se to nebi desilo trebamo reci pipenv-u da ignorira Pipfile i da koristi Pipfile.lock. To radimo sa 
# ? > pipenv install --ignore-pipfile
# dobijamo odgovor:
# ? Installing dependencies from Pipfile.lock (fe5a22)...
# ?   🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
# ? To activate this project's virtualenv, run pipenv shell.
# ? Alternatively, run a command inside the virtualenv with pipenv run.
# i sad mozemo biti sigurni da ce app raditi!