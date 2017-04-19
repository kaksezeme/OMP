import math


class Vektor:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_tocke(cls, t1,t2):
        x = t2.x - t1.x
        y = t2.y - t1.y
        z = t2.z - t1.z
        return cls(x, y, z)

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def scalar_with(self, v2):
        return self.x * v2.x + self.y * v2.y + self.z * v2.z

    def vector_product(self, v2):
        return Vektor((self.y * v2.z - self.z * v2.y), (self.z * v2.x - self.x * v2.z), (self.x * v2.y - self.y * v2.x))

    def paralel_with(self, v2):
        if self.vector_product(v2).length() == 0:
            return True
        else:
            return False

    def angle_with(self, v2):
        scalar = self.scalar_with(v2)
        lengths = self.length() * v2.length()
        return math.acos(scalar/lengths)

    def __eq__(self, v2):
        if self.x == v2.x and self.y == v2.y and self.z == v2.z:
            return True
        else:
            return False

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"
