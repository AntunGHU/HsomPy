# 3'58

# ne moramo sve atribute definirati u konstruktoru. Neke mozemo i kasnije kad god osjetimo potrebu za njima


class Point:
    default_color = "red "

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.z = 10
point.draw()    # Point (1, 2)

# atributi do sada su tzv "instance" atributi i klasni default_color

another = Point(3, 4)
another.draw()      # Point (3, 4)

# pozivanje klasnih atributa: kao i instancnih ali i kao klasnih
print(point.default_color)  # red
print(Point.default_color)  # red

# pokaz da se klasni atributi primjenjuju na sve instance: mjenjam boju klasnog atributa s upotrebom klase, i poslije provjeravam sa instancom i dobijem promjenjunu!

Point.default_color = "green"
print(point.default_color)  # green
