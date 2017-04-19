import math


class Vektor:
    x = None
    y = None
    z = None

    def __init__(self, t1, t2):
        self.x = t2.x - t1.x
        self.y = t2.y - t1.y
        self.z = t2.z - t1.z

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def __eq__(self, v2):
        if self.x == v2.x and self.y == v2.y and self.z == v2.z:
            return True
        else:
            return False

    def angle_with(self, v2):
        scalar = self.x * v2.x + self.y * v2.y + self.z * v2.z
        lengths = self.length() * v2.length()
        return math.acos(scalar/lengths)

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"
