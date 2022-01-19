import math

"""Zbytecna funkce, jen jsem se s ni delal, treba ji nekdy vyuziju"""

class Vector2(tuple):
    def __new__(cls, x, y):
        n = tuple.__new__(cls, (int(x), int(y)))
        n.x = x
        n.y = y
        return n

    def __add__(self, other):
        return self.__new__(type(self), self.x + other.x, self.y + other.y)


    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    @staticmethod
    def from_points(P1, P2):
        return Vector2(P2[0] - P1[0], P2[1] - P1[1])

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude