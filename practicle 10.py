import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x},{self.y})"
    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 +(self.y-other.y)**2)

x1 = float(input("Enter x for point 1: "))
y1 = float(input("Enter y for point 1: "))
x2 = float(input("Enter x for point 2: "))
y2 = float(input("Enter y for point 2: "))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print(p1)
print(p2)
print(f"Distance {p1.distance(p2)}")