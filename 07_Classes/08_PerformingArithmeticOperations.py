# 1'31

# dunderi za aritmetiku

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y)


point = Point(10, 20)
point2 = Point(1, 2)
combo = point + point2
print(combo)  # <__main__.Point object at 0x7fc585ba0f70>
print(combo.x)  # 11
