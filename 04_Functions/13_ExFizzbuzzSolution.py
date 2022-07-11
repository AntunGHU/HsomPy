# 4'41

# rjesio sam nakon par pokusaja sa zagradama i 15 kao 3. cim dok se nisam sjetio da py ide po redu pa stavio 15 na 1.mj. njegovo rjesenje je slicno ali sa and

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 ==0:
        return "FizzBuzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0:
        return "Fizz"
    return input
    
    
print(fizz_buzz(3))     # Fizz
print(fizz_buzz(10))    # Buzz
print(fizz_buzz(15))    # FizzBuzz
print(fizz_buzz(7))    # 7
print(fizz_buzz(8))