# 4'37


class Point:
    def __init__(self, x, y):   # constructor - funkcija koja kreira propse klase
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()    # Point (1, 2)

# propsi su kao boja ociju, visina i sl dok su metodi kao hodanje, gledanje itd!
# specificnost self-a je da ga ne moramo argumentirati kao druge parametre!
# kuriozitet:
point.draw(point) # moguce ali nepotrebno zbog innermachinery of Python koja sama dohvaca self!! tako tvrdi Mosh ali term se ne slaze
# TypeError: Point.draw() takes 1 positional argument but 2 were given
