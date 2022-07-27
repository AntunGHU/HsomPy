# 4'41

# Ath nam zeli pokazati cijenu raise-anja sa modulom timeit.
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be a zero ili manje!")  # Age...
    return 10 / 0


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print("code1=", timeit(code1, number=10000))
# ? Age cannot be a zero ili manje!
# ? Age cannot be a zero ili manje!
# ? Age cannot be a zero ili manje!
# ? Age cannot be a zero ili manje!
# ? Age cannot be a zero ili manje!
# ? code1= 0.3623867109999992

# sad isto to ali pass-amo umjesto "print(error)"
# ?  code1= 0.004098053002962843

# sad umjesto da raise-amo exception return-amo None a kod nazovemo code2, ne treba nam ni try blok nego ga mjenjamo sa if statement.

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / 0


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("code2=", timeit(code2, number=10000))
# ? Age cannot be a zero ili manje!

# Na kraju se pokazuje 2-3 puta razlika u vremenu:
code1 = 0.003282243007561192
code2 = 0.001539983000839129

# Zaljucak: ako pravimo jednostavan app, dizanje gresaka nece imati veliki utjecaj na perfomanse, ali ako pravimo app gdje je brzina bitna, rejzajmo samo kad bas moramo! Prvo vidi mozes li rjesiti problem sa if
