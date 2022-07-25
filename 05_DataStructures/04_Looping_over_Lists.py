# 2'54

letters = ["a", "b", "c", "d"]

for letter in letters:
    print(letter)

# ako zelimo dobiti i index svakog itema - "enumerate" - cija ce svaka iteracija dati tuple sa indexom i indexiranim!

for letter in enumerate(letters):
    # (0, 'a')(1, 'b')(2, 'c')(3, 'd') (jedan spod drugog ofcourse!)
    print(letter)


for letter in enumerate(letters):
    print(letter[0])                # 0 1 2 3

for letter in enumerate(letters):
    print(letter[0], letter[1])     # .0 a
# .....................................1 b
# .....................................2 c
# .....................................3 d

# varijacija na temu

for index, letter in enumerate(letters):
    print(index, letter)            # .0 a
# .....................................1 b
# .....................................2 c
# .....................................3 d
