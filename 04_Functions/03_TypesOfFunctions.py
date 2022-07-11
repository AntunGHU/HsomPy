# 4'02

def greet(name):
        print(f"Hello {name}")
    
greet("Antun")

# 1)"Perform a Task" funcs kao gornji primjer; 2)"Return a value" funcs kao round dole

a=round(1.98765, 2)
print(a)

# kako rewritati 1) u 2)

def get_greeting(name):
        return f"Hi {name}"
    
message = get_greeting("Antun")
print(message)

# 2) forma funsa je bolja jer mozemo sa njenomreturn-value raditi sto hocemo, pa i printati ili malo busanja sa "open" i pisanja u fajl!
# za kraj malo oko printa od printa

def greet(name):
        print(f"Hello {name}")
    
print(greet("Antun"))   # Hello Antun i " None" !?!? None u py je default-return value svake funkcije i reprezentira odsustvo return-value-a osim ako se specificno ne navede return-value (kao u ovom slucaju "f...")