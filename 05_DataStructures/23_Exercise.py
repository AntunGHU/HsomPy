from pprint import pprint


sentence = "This is a common interview question"
# ucestalost = {c:count(c) for c in sentence}
# print(ucestalost)

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# {'T': 1, 'h': 1, 'i': 5, 's': 3, ' ': 5, 'a': 1, 'c': 1, 'o': 3, 'm': 2, 'n': 3, 't': 2, 'e': 3, 'r': 1, 'v': 1, 'w': 1, 'q': 1, 'u': 1}
print(char_frequency)

# posto je malo necitko Mash nam daje trik:
pprint(char_frequency, width=1)  # .{' ': 5,
# .................................. 'T': 1,
# .................................. 'a': 1,
# .................................. 'c': 1,
# .................................. 'e': 3,
# .................................. 'h': 1,
# .................................. 'i': 5,
# .................................. 'm': 2,
# .................................. 'n': 3,
# .................................. 'o': 3,
# .................................. 'q': 1,
# .................................. 'r': 1,
# .................................. 's': 3,
# .................................. 't': 2,
# .................................. 'u': 1,
# .................................. 'v': 1,
# .................................. 'w': 1}

# kako bi dict sortirali po ucestalosti pojedinog slova moramo svaki "key-value" par pretvoriti u tuple a citav dict u listu tuplova. Tada cemo ih moci sortirati. To cemo uciniti sa metodom "sorted" koji vraca listu-tuplove.

print(sorted(char_frequency.items()))  # izlaz dole
# [(' ', 5), ('T', 1), ('a', 1), ('c', 1), ('e', 3), ('h', 1), ('i', 5), ('m', 2), ('n', 3), ('o', 3), ('q', 1), ('r', 1), ('s', 3), ('t', 2), ('u', 1), ('v', 1), ('w', 1)]
# # dobili smo listu tuplova koja po def-u nije sortirana jer "sortied" nije imao instrukcije za sortiranje! Ali ako mu dodamo key za sortiranje pomocu lambda funkcije
print(sorted(char_frequency.items(), key=lambda kv: kv[1]))
# [('T', 1), ('h', 1), ('a', 1), ('c', 1), ('r', 1), ('v', 1), ('w', 1), ('q', 1), ('u', 1), ('m', 2), ('t', 2), ('s', 3), ('o', 3), ('n', 3), ('e', 3), ('i', 5), (' ', 5)]
# i sad nam jos preostaje reversed-ati sortanje
print(sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))
# [('i', 5), (' ', 5), ('s', 3), ('o', 3), ('n', 3), ('e', 3), ('m', 2), ('t', 2), ('T', 1), ('h', 1), ('a', 1), ('c', 1), ('r', 1), ('v', 1), ('w', 1), ('q', 1), ('u', 1)]
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)

print(char_frequency_sorted[0])  # ('i', 5) # nas konacan odgovor!!!
