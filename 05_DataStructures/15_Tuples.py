# 4'02

# Tuples are read-only lists!!!
point = (1, 2)
# ali malo mashine, i bez () je tuple

troint = 1, 2, 3
print(type(troint))  # <class 'tuple'>

oint = 1,       # zarez presudan!
print(type(oint))  # <class 'tuple'>

noint = ()       # i same zagrade
print(type(noint))  # <class 'tuple'>

tapel = (1, 2) + (3, 4)  # konkatinacija
print(tapel)        # (1, 2, 3, 4)

tapel = (1, 2) * 3  # mnozenje radi ponavljanja
print(tapel)        # (1, 2, 1, 2, 1, 2)

utapel = tuple([1, 2, 3, 4])
print(utapel)       # (1, 2, 3, 4)

utapel = tuple("Hello World")
print(utapel)       # ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

# Dohvacanja
print(utapel[7])        # o
print(utapel[1:7])        # ('e', 'l', 'l', 'o', ' ', 'W')
x, y, z, *others = utapel
print(x, y, z)  # H e l
if "H" in utapel:
    print("exists")

utapel[0] = "R"  # TypeError: 'tuple' object does not support item assignment
