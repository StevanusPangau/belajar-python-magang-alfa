"""Overloading Operator
Dalam Python, Anda dapat melakukan overloading operator dengan mendefinisikan metode-metode khusus yang memiliki nama yang ditentukan, seperti:

__add__ untuk operator penambahan +
__sub__ untuk operator pengurangan -
__mul__ untuk operator perkalian *
__truediv__ untuk operator pembagian /
__lt__ untuk operator kurang dari <
__le__ untuk operator kurang dari atau sama dengan <=
__eq__ untuk operator sama dengan ==
__ne__ untuk operator tidak sama dengan !=
__gt__ untuk operator lebih dari >
__ge__ untuk operator lebih dari atau sama dengan >=
Dan lain-lain.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __str__(self) -> str:
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)


a = Point(10, 3)
b = Point(2, 7)
c = Point(8, 1)

print(a)
print(a + b)
print(c - b)
print(a * b)
