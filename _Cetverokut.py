class Cetverokut:
    A = None
    B = None
    C = None
    D = None

    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def __str__(self):
        return "A" + str(self.A) + " B" + str(self.B) + " C" + str(self.C) + " D" + str(self.D)

