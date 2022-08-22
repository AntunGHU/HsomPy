# 4'05

# Slicno kao i s atributima pozivanje pocinje sa imenom klase

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)    # ekvivalent pisanja Point(0,0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1,2)
point.draw()    # Point (1, 2)

# klas metod koristimo npr kad zelimo inicijalne vrijednosti point-a (0,0). 
# Njih bi mogli kreirajuci objekt i stavljajuci "point = Point(0,0" ali mozemo i s klasmetodom kao gore! i pozivanjem kao dole

Point.zero() # i time je svaki objekt kreiran iza dobio pocetno (0,0) tako da
point=Point.zero() # ima (0,0) iako to nismo posebno instantirali! pozivanje navodjenjem imaena klase ili cls
point.draw() # (0,0)