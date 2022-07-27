# 3'11

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)

print(point == other)   # False pa True

# ponovo na superstranicu i poblize u odjeljak "comparison magic methods"
# sada nakon nadopune sa dunderom eq oni postaju ==

# prosiruje sa pokusajem >
# TypeError: '>' not supported between instances of 'Point' and 'Point'
print(point > other)    # False a nakon izmjene koordinata True

# zato opet idemo nadopuniti klasu sa novim dudnderom "gt" (greater than) poslije kojeg umjesto error dobijemo True - False
