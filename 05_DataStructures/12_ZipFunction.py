# 1'49

list1 = [1, 3, 5]
list2 = ["a", "b", "c"]

kombo = zip(list1, list2)
print(kombo)  # <zip object at 0x7fba4e13b900>
print(list(kombo))  # [(1, 'a'), (3, 'b'), (5, 'c')]

# i malo Mashovshtine
kombo = zip("abc", list1, list2)
print(list(kombo))  # [('a', 1, 'a'), ('b', 3, 'b'), ('c', 5, 'c')]
