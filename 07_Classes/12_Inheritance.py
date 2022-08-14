# 4'32

# DRY: Dont repeat yourself
# Kako bi DRY princip proveli posezemo za 1)Inheritance ili 2)Composition

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mamal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mamal()
m.eat()
m.walk()
print(m.age)   # 1
