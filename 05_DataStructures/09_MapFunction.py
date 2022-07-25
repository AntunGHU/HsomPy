# 3'25

items = [
    ("pr1", 10),
    ("pr2", 9),
    ("pr3", 8)
]
items.sort()

# recimo da zelimo iz "items"a izvuci samo cijene i od njih formirati listu cjena

prices = []

for item in items:
    prices.append(item[1])

print(prices)       # [10, 9, 8]

# elegantniji nacin je sa builtin "map" fn

x = map(lambda item: item[1], items)
print(x)        # <map object at 0x7f8c4fda47f0>

# ali ako sad dodamo funkciju list
prices = list(map(lambda item: item[1], items))
print(prices)        # [10, 9, 8]
