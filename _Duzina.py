import numpy as np
from _Vektor import Vektor
from _Tocka import Tocka


class Duzina:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sjeciste(self, druga_duzina):
        vektor_smjera_1 = Vektor.from_tocke(self.a, self.b)
        vektor_smjera_2 = Vektor.from_tocke(druga_duzina.a, druga_duzina.b)

        if vektor_smjera_1.paralel_with(vektor_smjera_2):
            return None

        tocka_presjeka = self.get_tocka_presjeka(vektor_smjera_1, vektor_smjera_2, druga_duzina)

        v1 = Vektor.from_tocke(self.a, tocka_presjeka)
        v2 = Vektor.from_tocke(druga_duzina.a, tocka_presjeka)

        kof1 = self.get_koeficjent(v1, vektor_smjera_1)
        kof2 = self.get_koeficjent(v2, vektor_smjera_2)

        if kof1 >= 0 and kof1 <= 1 and kof2 >= 0 and kof2 <= 1:
            return tocka_presjeka
        else:
            return None

    def get_tocka_presjeka(self, vektor_smjera_1, vektor_smjera_2, druga_duzina):
        a = [[vektor_smjera_1.x, -vektor_smjera_2.x],
             [vektor_smjera_1.y, -vektor_smjera_2.y],
             [vektor_smjera_1.z, -vektor_smjera_2.z]]
        b = [druga_duzina.a.x - self.a.x, druga_duzina.a.y - self.a.y, druga_duzina.a.z - self.a.z]

        t = np.linalg.lstsq(a, b)[0][0]

        return Tocka(self.a.x + vektor_smjera_1.x * t, self.a.y + vektor_smjera_1.y * t,
                     self.a.z + vektor_smjera_1.z * t)

    def get_koeficjent(self, v, s):
        koef = 0.0

        if s.x == 0 and s.y == 0 and s.z == 0:
            if v.x == 0 and v.y == 0 and v.z == 0:
                return 0
        elif s.x != 0:
            koef = v.x / s.x
        elif s.y != 0:
            koef = v.y / s.y
        elif s.z != 0:
            koef = v.z / s.z

        return koef