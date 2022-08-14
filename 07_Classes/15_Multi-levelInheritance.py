# 2'42

# previse dobrog je lose pa tako i sa inheritance: povecava se kompleksnost koda!
# Ako inheritamo preporuka je 1 do najvise 2 level-a inace pucat cete si u nogu!

class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass

# ali!!! pile ne moze letjeti i vec smo neprecizni!!!
