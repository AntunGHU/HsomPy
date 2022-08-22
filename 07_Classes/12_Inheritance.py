# 4'32

# DRY: Dont repeat yourself
# Kako bi DRY princip proveli posezemo za 1)Inheritance - ovdje ili 2)Composition - kasnije

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

# inheritance olaksava ispravljanje bagova - radimo samo u parent-klasi a ne na child klasama!!!