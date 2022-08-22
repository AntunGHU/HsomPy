# 3'45

# Pascal naming convention: Prvo veliko slovo a ako vise rijeci onda CamelCase

class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))  # <class '__main__.Point'>
print(isinstance(point, Point))  # True
print(isinstance(point, int))  # False
