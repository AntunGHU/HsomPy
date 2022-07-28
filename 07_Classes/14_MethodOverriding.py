# 3'14

class Animal:
    def __init__(self):
        print("Animal init")
        self.age = 1

    def eat(self):
        print("eat")


class Mamal(Animal):
    def __init__(self):
        super().__init__()
        print("Mamal init")
        self.weight = 2

    def walk(self):
        print("walk")


m = Mamal()
# print(m.age)    # AttributeError: 'Mamal' object has no attribute 'age'
# Dakle, init Mamala je overridao init Animal-a! Ako ne zelimo da se to desi moramo posebno koristenjem linije "super()" pozvati i init Animal-a
print(m.weight)  # 2 -radi posle dodavanja super()
print(m.age)  # 1 - radi posle dodavanja super()


# Animal init; Mamal init; 2; 1
# poredak ovisi o poretku super() u constructoru Mamal-a!
