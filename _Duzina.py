import numpy as np
from _Vektor import Vektor
from _Tocka import Tocka


class Duzina:
    a = None
    b = None

    def __init__(self, a, b):
        """
        :param a: Tocka a trenutne duzine
        :param b: Tocka b trenutne duzine
        """
        self.a = a
        self.b = b

    @classmethod
    def from_list(cls, l):
        """
        :param l: lista s kordinatama tocaka a(l[0], l[1]) i b(l[2], l[3]) 
        :return: Duzina definirana tockama a i b
        """
        a = Tocka(l[0], l[1])
        b = Tocka(l[2], l[3])
        return cls(a, b)

    def __str__(self):
        """
        :return: string ispis trenutne Duzine u kordinatama
        """
        return "[(" + str(self.a.x) + ", " + str(self.a.y) + ", " + str(self.a.z) +")(" + str(self.b.x) + ", " + str(self.b.y) + ", " + str(self.b.z) + ")]"

    def length(self):
        """
        :return: float duljina trenutne duzine   
        """
        return Vektor.from_tocke(self.a, self.b).length()

    def get_sjeciste_s_duzinom(self, druga_duzina):
        """
        :param druga_duzina: duzina za koju treba odrediti sjece li se s trenutnom duzinom 
        :return: Tocka ako se duzine sjeku; None ako se duzine ne sjeku
        """
        vektor_smjera_1 = Vektor.from_tocke(self.a, self.b)
        vektor_smjera_2 = Vektor.from_tocke(druga_duzina.a, druga_duzina.b)

        if vektor_smjera_1.paralel_with(vektor_smjera_2):
            return None

        tocka_presjeka = self.get_tocka_presjeka(vektor_smjera_1, vektor_smjera_2, druga_duzina)

        if self.sjeciste_u_tockama_duzina(tocka_presjeka, druga_duzina):
            return tocka_presjeka

        v1 = Vektor.from_tocke(self.a, tocka_presjeka)
        v2 = Vektor.from_tocke(druga_duzina.a, tocka_presjeka)

        kof1 = self.get_koeficjent(v1, vektor_smjera_1)
        kof2 = self.get_koeficjent(v2, vektor_smjera_2)

        if 0 < kof1 <= 1 and 0 < kof2 <= 1:
            return tocka_presjeka
        else:
            return None

    def get_tocka_presjeka(self, vektor_smjera_1, vektor_smjera_2, druga_duzina):
        """
        :param vektor_smjera_1: vektor smjera pravca na kojem se nalazi trenutna duzina 
        :param vektor_smjera_2: vektor smjera pravca na kojem se nalazi druga duzina
        :param druga_duzina: druga duzina 
        :return: Tocka koja predstavlja tocku presjeka trenutne duzine i druge duzine
        """
        a = [[vektor_smjera_1.x, -vektor_smjera_2.x],
             [vektor_smjera_1.y, -vektor_smjera_2.y],
             [vektor_smjera_1.z, -vektor_smjera_2.z]]
        b = [druga_duzina.a.x - self.a.x, druga_duzina.a.y - self.a.y, druga_duzina.a.z - self.a.z]

        t = np.linalg.lstsq(a, b)[0][0]

        return Tocka(self.a.x + vektor_smjera_1.x * t, self.a.y + vektor_smjera_1.y * t,
                     self.a.z + vektor_smjera_1.z * t)

    def sjeciste_u_tockama_duzina(self, tocka_presjeka, druga_duzina):
        if tocka_presjeka == self.a or tocka_presjeka == self.b \
                or tocka_presjeka == druga_duzina.a or tocka_presjeka == druga_duzina.b:
            return True
        else:
            return False

    def get_koeficjent(self, v, s):
        """
        :param v: prvi vektor
        :param s: drugi vektor
        :return: float - faktor produljenja izmedu vektora v i vektora s
        """
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