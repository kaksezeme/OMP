class Tocka:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def mid(self, t2):
        x_mid = (self.x + t2.x) / 2
        y_mid = (self.y + t2.y) / 2
        z_mid = (self.z + t2.z) / 2
        return Tocka(x_mid, y_mid, z_mid)

    def __eq__(self, other):
        if other == None:
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"