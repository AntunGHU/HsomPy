# 2'56

letters = ["a", "b", "c", "d"]

# Add na kraj

letters.append("1")
print(letters)      # ['a', 'b', 'c', 'd', '1']


# na odredjeno mjesto

letters.insert(2, "2")
print(letters)      # ['a', 'b', '2', 'c', 'd', '1']

# removanje s kraja

letters.pop()
print(letters)      # ['a', 'b', '2', 'c', 'd']

# removanje s indexom
letters.pop(0)
print(letters)      # ['b', '2', 'c', 'd']

# removanje bez indexa
letters.remove("c")
print(letters)      # ['b', '2', 'd']

# brisanje vise odjednom
letters = ["a", "b", "c", "d", "e", 1, 2]
del letters[3:5]
print(letters)      # ['a', 'b', 'c', 1, 2]

# brisanje svega
letters.clear()
print(letters)      # []
