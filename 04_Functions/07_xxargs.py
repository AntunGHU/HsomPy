# 2'20

def save_user(**user):   # naravno radi orginalnosti cijelo vrijeme je sa numbres a ne args kako je obicaj!
    print(user)     
    
save_user(name="antun", last="Jerak", star=59)  # {'name': 'antun', 'last': 'Jerak', 'star': 59}

# objasnjenje je da pasamo key-word argumente. Bum! Mladicu moj, mora se u nekom trenutku bombardirati. Nekad treba zvakati. Nemozes sve dobiti vec prezvakano! Osim toga spominje i dictionaries!

# a sad finesa o tome kako dobiti value navodjenjem key-a

def save_user(**user):  
    print(user["name"])     
    
save_user(name="antun", last="Jerak", star=59) # antun -sama vrijednost, nema vise dict-a