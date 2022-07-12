# 1'35

#? def increment(broj=100, za):    # moj 1. pokusaj pravi gresku redosljeda: ne moze doci default ispred obicnog paranmetra
#?     return broj + za

# stavljanjem defaulta od parametra ne moramo ga unositi kao argument

def increment(broj, za=100): 
    return broj + za
print(increment(1))

# ali ako zeli drugaciji "za" samo ga dodam u poziv

def increment(broj, za=100): 
    return broj + za
print(increment(1, 200))