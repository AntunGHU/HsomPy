# 4'15

def multiply(*numbers):
    print(numbers)
    
multiply(2,3,4,5)   # (2,3,4,5) # i malo pilanja oko tuple-a, ni najbolji ne mogu izbjeci komplikacije slozenih stvari!

# obzirom na kompleksniji ulaz dolazi do prekodiranja funsa

def multiply(*numbers):
    for number in numbers:
        print(number)
    
multiply(2,3,4,5)   # 2,3,4,5 jedan ispod drugog

# sada konacna varijanta radi izracuna umnoska:

def multiply(*numbers):
    total =  1
    for number in numbers:
        total*= number
    return total
    
print(multiply(2,3,4,5))