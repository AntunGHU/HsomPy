# 1'31

# dunderi za aritmetiku: ovdje omogucavamo zbrajanje unutar nase klase Point

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y)
    
    def __str__(self):
        return f"{self.x}, {self.y}"



point = Point(10, 20)
point2 = Point(1, 2)
print(point + point2)   # 11,22

combo = point + point2
print(combo)  # 11,22 (prije dopune sa str-dunderom combo je bio: <__main__.Point object at 0x7fc585ba0f70>)
print(combo.x)  # 11
