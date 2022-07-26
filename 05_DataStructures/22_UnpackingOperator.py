# 4'05

# misli na *-operator

numbers = [1, 2, 3]
print(numbers)  # [1, 2, 3]

# ali ako hocu da dobijem ala
print(1, 2, 3)      # 1 2 3

# koristimo *
print(*numbers)      # 1 2 3  u js to je spread ...

# mozemo ga koristiti na bilo kom iterableu a ne samo na listama
values = [*range(5)]
print(values)   # [0, 1, 2, 3, 4]

# ili
values = [*range(5), *"Hello"]
print(values)       # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

# ili kobinirati iterablese
first = [1, 2, 3]
second = [4, 5]
kombo = [*first, *second]
kombo1 = [*first, "a",  *second, *"Hello"]
print(kombo)    # [1, 2, 3, 4, 5]
print(kombo1)    # [1, 2, 3, 'a', 4, 5, 'H', 'e', 'l', 'l', 'o']

# raspakirati mozemo i dicte ali moramo koristiti **
prvi = {"X": 1}
drugi = {"X": 10, "z": 100}
combo = {**prvi, **drugi, "a": 2}
# {'X': 10, 'z': 100, 'a': 2} # ako imamo vise key-eva istog imena, zadnji namece svoju vrijednost!
print(combo)
