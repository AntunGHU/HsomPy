# 1'29

# problem fizzbuzz-algoritam koji ni mnogi iskusniji progsi ne znaju rjesiti a jako cesto dolazi na intervjuima za  posao!
# pravila:  -ako je input djeljiv s 3 vraca string "fizz"
#           -ako je djeljiv s 5 vraca "Buzz"
#           -ako je djeljiv i sa 3 i sa 5 vraca "FizzBuzz"
#           -za sve druge brojeve vraca te brojeve same

def fizz_buzz(input):
    if input % 15 == 0:
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
print(fizz_buzz(8))     # 8
