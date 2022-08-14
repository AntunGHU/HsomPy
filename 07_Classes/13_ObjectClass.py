# 2'23

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mamal(Animal):
    def walk(self):
        print("walk")


m = Mamal()
m.eat()
m.walk()
m.age   # 1

print(isinstance(m, Mamal))  # True
print(isinstance(m, Animal))  # True

# do sad je sve evidentno. Ono sto ova lekcija donosi je da klasa Animal takodjer nasljedjuje od klase object!!! iako to nije upisano u zagrade. Klasa object je base-klasa svih klasa u Py!

print(isinstance(m, object))  # True
o = object()
# i ako sad provociramo s tockom "o." intelisense pojavljuju se svi moguci dunderi!

print(issubclass(Mamal, Animal))  # True
print(issubclass(Mamal, object))  # True
