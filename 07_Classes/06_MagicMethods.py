# 3'13

# dok cemo ovdje pogledati neke za vise googlaj sa "python 3 magic methods" sto ce nam dati pristup stranici https://rszalski.github.io/magicmethods/ koju mosh smatra boljom od py-doc jer je kategorizirano i klasificirano. Priomjer sa repr. Potom pokazuje kako i mi mozemo defati dundere:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()    # Point (1, 2)

print(point)  # 1,2 a ne kao prije <__main...

# dunder se mozue koristiti i na sljedeci nacin

print(str(point))  # 1,2
