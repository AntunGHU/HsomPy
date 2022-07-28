# 3'22

class Employee:
    def greet(self):
        print("Employee greet")


class Person:
    def greet(self):
        print("Person greet")


class Manager(Employee, Person):
    pass

# ovo se zove multiple Inheritance i slicno kao i Multilevel inheritance, moze biti izvor niza problema!


m = Manager()
m.greet()  # Employee greet # zato jer je bio prvi

# ako sutra neki programer promjeni poredak nas ce app imati drugacije ponasanje!?!?
# zasto to onda imamo? zato sto ima dobrih strana!!! Primjer


class Flyer:
    def fly(self):
        pass


class Swimer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimer):
    pass
