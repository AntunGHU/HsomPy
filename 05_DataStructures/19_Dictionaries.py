# 5'24

# Key-value pairs (key samo strings and numbers, ali values of any type)
point = dict(x=1, y=2)
print(point)    # {'x': 1, 'y': 2}

print(point["x"])   # 1

point["x"] = 10
print(point)    # {'x': 10, 'y': 2}

point["z"] = 100
print(point)    # {'x': 10, 'y': 2, 'z': 100}

# print(point["a"])   # KeyError: 'a'

if "a" in point:
    print(point["a"])

print(point.get("a"))   # None  ili
print(point.get("a", 0))   # 0

del point["x"]
print(point)    # {'y': 2, 'z': 100}

# loopanje u dict po defu ide po key-sima
for x in point:
    print(x)        # y, z

# zato je normalno pisati
for key in point:
    print(key, point[key])  # y 2; z 100

# drugi nacin iteriranja
for x in point.items():
    print(x)        # ('y', 2); ('z', 100)  #tupli sa key,value pa zato

# uobicajenije pisanje

for key, value in point.items():
    print(key, value)       # ('y', 2); ('z', 100)
