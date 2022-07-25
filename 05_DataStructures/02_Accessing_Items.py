# 3'13

letters = ["a", "b", "c", "d"]

letters[0]  # "a"
letters[0] = "A"

print(letters)  # ['A', 'b', 'c', 'd']

print(letters[0:3])  # ['A', 'b', 'c']
print(letters[:])  # ['A', 'b', 'c', 'd']
print(letters[::2])  # ['A', 'c']
print(letters[::-1])  # ['d', 'c', 'b', 'A']

print(letters)  # ['A', 'b', 'c', 'd']  # stara lista nije se promjenila
