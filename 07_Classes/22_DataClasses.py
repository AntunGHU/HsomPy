# 4'36

from collections import namedtuple

# standardne klase uglavnom imaju data, metode itd kao cjelina, ali, postoje klase koje nemaju nikakve metode nedo samo datas!! Primjer


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)   # False # razlicite mem-lokacije! Dokaz dole
print(id(p1))       # 139838110939312
print(id(p2))       # 139838110994144

# medjutim, ako prosirimo klasu Point sa __eq__ oni mogu postati equal


class Pointe:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Pointe(1, 2)
p2 = Pointe(1, 2)
print(p1 == p2)   # True iako u mmemoriji i dalje egzistiraju kao razliciti
print(id(p1))       # 139838110939312
print(id(p2))       # 139838110994144

# medjutim pisati sav ovaj kod za "data"-klase je dosadno pa kod takvih mozemo koristiti "namedtuple" -funkciju koja se importa iz  "collections"-a. Vidi gore

Pointi = namedtuple("Pointi", ["x", "y"]) # Pointi-string: ime klase koja ima samo datas; []-lista stringova-imena atributa
p3 = Pointi(x=1, y=2)   # obavezno koristenje key-word argumenata!!!
p4 = Pointi(x=1, y=2)
print(p4.y) # 2
print(p3 == p4)     # True

# Dakle, ako radimo sa klasama koje imaju samo datas (atribute) imamo mogucnost koristenja funkcije namedtuple kad cemo pisati manje koda!!!! 