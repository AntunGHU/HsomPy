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
point.z = 10    # naknadno kreiranje 3. tocke z!!! x,y pripadaju instancama (point, another) a z samo z-eu!
point.draw()    # Point (1, 2)

# atributi do sada su tzv "instancni" atributi i 1 klasni default_color atribut

another = Point(3, 4)
another.draw()      # Point (3, 4)

# pozivanje klasnih atributa mozemo kroz-uz ime klase ali i kroz-uz ime svake instance
print(point.default_color)  # red
print(Point.default_color)  # red

# pokaz da se klasni atributi primjenjuju uz sve instance: mjenjam boju klasnog atributa s upotrebom klase, i poslije provjeravam sa instancom i dobijem promjenjunu!
Point.default_color = "green"
print(point.default_color)  # green
print(another.default_color)  # green
