# 2'05

items = [
    ("pr1", 10),
    ("pr2", 9),
    ("pr3", 12)
]
items.sort()

# zelimo npr samo cijene >= 10

x = filter(lambda item: item[1] >= 10, items)
print(x)    # <filter object at 0x7f71a38d57f0>

# i ako dodamo list

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)    # [('pr1', 10), ('pr3', 12)]
