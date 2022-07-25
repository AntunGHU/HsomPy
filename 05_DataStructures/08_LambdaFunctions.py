# 1'49

items = [
    ("pr1", 10),
    ("pr2", 9),
    ("pr3", 8)
]
items.sort()
print(items)        # [('pr1', 10), ('pr2', 9), ('pr3', 8)] jer py ne zna!
# u ovakvim slucajevima defamo funkcije za sortanje!


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)        # [('pr3', 8), ('pr2', 9), ('pr1', 10)]

# defanje funkcije kao medjukoraka za sortiranje moze se izbjeci upotrebom anonimnih funkcija tj lambde:

items2 = [
    ("pr1", 10),
    ("pr2", 9),
    ("pr3", 8)
]

items.sort(key=lambda item: item[1])
print(items)        # [('pr3', 8), ('pr2', 9), ('pr1', 10)]
# dakle, ono sto sam pokusao seljacki u osnovi radi ali tako da funkciju nazovem "lambda"
