# 3'10

# kao zgodan nastavak na mapiranja kroz map i filter je LC koji to sve isto moze i kojeg necemo sretati u drugim pr. jezicima
items = [
    ("pr1", 10),
    ("pr2", 9),
    ("pr3", 12)
]
prices = list(map(lambda item: item[1], items))
print(prices)
prices = [item[1] for item in items]
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
filtered = [item for item in items if item[1] >= 10]
print(filtered)
