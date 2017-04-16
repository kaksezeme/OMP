class Tocka:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mid(self, t2):
        x_mid = (self.x + t2.x) / 2
        y_mid = (self.y + t2.y) / 2
        return Tocka(x_mid, y_mid)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"