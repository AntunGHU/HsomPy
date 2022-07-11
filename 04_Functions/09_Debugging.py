# 6'50

# najduzi video do sada. Namjerna greska je u neispravnom identanju return-a. Debug pocinje s na Debug-view generiranjem fajla "launch.json" (klik na plavo "create a launch.json" i biranjem opcije "Python File debug currently active python file "). 
# Ne moramo ga editirati i zatvaramo ga! Mapa ./vscode/launch.json pojavljuje se u root-u projekta
# Debug pocinje s klik Debugview, Debugstarter (padajuci izbornik sa vise opcija, kod mene samo PyFile a kod njega i Py:Attach, Py:Module itd, Py:CurrentFile(integrated term), Py:CurrentFile(extrnal term)), klik na CurrentFile
# Dodavanje BP smjestanjem kursora na zeljenu liniju i F9 (ili klik misa ispred broja L)
# klik F5 (ili na zeleni runner) kako bi app isao do BP (orange ststus, ispisi izvrsenih linija u variables, call stack, breakpoints). Staje kod BP i pretvara se u klizac. Na terminalu je ispisano Start
# Na varijablama vidimo da je total dosao do 1 i program je stao (zato sto je iza njega bio return a to ima posljedice kao i break)
# Sada idemo korak po korak koristenjem duple vrijednosti F10 ili StepOver strelice. Prvo dolazimo do multiply(1,2,3) poziva. Ako ponovno F10 izvodjenje staje (plavi status itd) i nista nismo skuzili. Zato ponovo
# F5, F10 i sad ne zelimo iskljuciti nego uci u poziv sa F11 ili strelica Into (u VARIABLE se pojavljuju: numbers: (1,2,3) tuple argument, total jos nije jer je klizac tek na njemu, nakon naseg sljedeceg F10 pojavljuje se total: 1), ponovni F10 i ponovo out (najzad nas bug jos uvjek postoji ali sad znamo da je u funkciji tj u loop-u)
# Kod mene automatski izvan funkcije on pritiska SHIFT F5. Znaci nas loop se nije izveo i znamo gdje traziti gresku. Popravljamo, snimamo i ponovo run in Debug mode: I sve ok
# Tip: ovdje smo BP stavili na start ali ako znamo gdje bi mogao biti problem BP mozemo odmah tamo! na L16 pa ce odmah uci u fu kciju! Ako smo u funkciji i znamo da je tamo sve ok, ne moramo cekati loop nego mozemo odmah izaci sa SHIFT F11 ili strelicom Out

 
def multiply(*numbers):
    total =  1
    for number in numbers:
        total*= number
    return total

print("Start")    
multiply(1,2,3)