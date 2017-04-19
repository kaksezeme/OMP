import numpy as np
from _Vektor import Vektor
from _Tocka import Tocka


class Duzina:
    a = None
    b = None

    def __init__(self,a, b):
        self.a = a
        self.b = b

    def get_sjeciste(self, d2):
        s1 = Vektor.from_tocke(self.a, self.b)
        s2 = Vektor.from_tocke(d2.a, d2.b)

        if s1.paralel_with(s2):
            return None

        s = Tocka(0,0)
        return s
