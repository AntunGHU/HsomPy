# 3'19

values = []
for x in range(5):
    values.append(x*2)

# isto sa LC, ali i SetComprehension i DictComprehension

values = [x*2 for x in range(5)]
print(values)   # [0, 2, 4, 6, 8]
values = {x*2 for x in range(5)}
print(values)   # {0, 2, 4, 6, 8}
values = {x: x*2 for x in range(5)}
print(values)   # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# medjutim ako to probamo za tuple, ne ide, dobijemo nesto drugo!
values = (x*2 for x in range(5))
print(values)   # <generator object <genexpr> at 0x7ff9e5c64890>
