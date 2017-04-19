from _Vektor import *


class Cetverokut:
    a = None
    b = None
    c = None
    d = None

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return "A" + str(self.a) + " B" + str(self.b) + " C" + str(self.c) + " D" + str(self.d)

    def klasifikacija(self):
        tipovi = []

        if self.jel_konveksni():
            tipovi.append("Konveksni")
        if self.jel_konkavni():
            tipovi.append("Konkavni")
        if self.jel_pravokutnik():
            tipovi.append("Pravokutnik")
        if self.jel_paralelogram():
            tipovi.append("Paralelogram")
        if self.jel_romb():
            tipovi.append("Romb")
        if self.jeli_kvadrat():
            tipovi.append("Kvadrat")
        if self.jel_tetivni():
            tipovi.append("Tetivni cetverokut")
        if self.jel_tangencijalni():
            tipovi.append("Tangencijalni cetverokut")
        return tipovi

    def jel_pravokutnik(self):
        ab = Vektor.from_tocke(self.a, self.b)
        bc = Vektor.from_tocke(self.b, self.c)
        cd = Vektor.from_tocke(self.c, self.d)
        da = Vektor.from_tocke(self.d, self.a)

        if ab.length() == cd.length() and bc.length() == da.length() and ab.angle_with(bc) == math.pi / 2:
            return True
        else:
            return False

    def jel_paralelogram(self):
        ab = Vektor.from_tocke(self.a, self.b)
        dc = Vektor.from_tocke(self.d, self.c)
        ad = Vektor.from_tocke(self.a, self.d)
        bc = Vektor.from_tocke(self.b, self.c)

        if ab == dc and ad == bc and ab.angle_with(bc) != math.pi / 2:
            return True
        else:
            return False

    def jel_konveksni(self):
        v1 = Vektor.from_tocke(self.a, self.b)
        v2 = Vektor.from_tocke(self.a, self.d)
        v3 = Vektor.from_tocke(self.b, self.a)
        v4 = Vektor.from_tocke(self.b, self.c)
        v5 = Vektor.from_tocke(self.c, self.b)
        v6 = Vektor.from_tocke(self.c, self.d)
        v7 = Vektor.from_tocke(self.d, self.c)
        v8 = Vektor.from_tocke(self.d, self.a)
        zbroj = v1.angle_with(v2) + v3.angle_with(v4) + v5.angle_with(v6) + v7.angle_with(v8)
        if zbroj == 2 * math.pi:
            return True

        return False

    def jel_konkavni(self):
        if self.jel_konveksni():
            return False
        else:
            return True

    def jel_romb(self):
        ab = Vektor.from_tocke(self.a, self.b)
        dc = Vektor.from_tocke(self.d, self.c)
        ad = Vektor.from_tocke(self.a, self.d)
        bc = Vektor.from_tocke(self.b, self.c)
        sjeciste_dijagonala = self.a.mid(self.c)

        v5 = Vektor.from_tocke(sjeciste_dijagonala, self.a)
        v6 = Vektor.from_tocke(sjeciste_dijagonala, self.d)

        dijagonala1 = Vektor.from_tocke(self.a, self.c)
        dijagonala2 = Vektor.from_tocke(self.b, self.d)

        if ab == dc and ad == bc and ab.length() == ad.length() and v5.angle_with(v6) == math.pi / 2 \
                and dijagonala1.length() != dijagonala2.length():
            return True
        else:
            return False

    def jeli_kvadrat(self):
        ba = Vektor.from_tocke(self.b, self.a)
        cd = Vektor.from_tocke(self.c, self.d)
        bc = Vektor.from_tocke(self.b, self.c)
        ac = Vektor.from_tocke(self.a, self.c)

        dijagonala = ba.length() * math.sqrt(2)

        if ba == cd and ba.angle_with(bc) == math.pi/2 and dijagonala == ac.length():
            return True
        else:
            return False

    def jel_tetivni(self):
        kut_a = Vektor.from_tocke(self.a, self.b).angle_with(Vektor.from_tocke(self.a, self.d))
        kut_c = Vektor.from_tocke(self.c, self.b).angle_with(Vektor.from_tocke(self.c, self.d))

        if kut_a + kut_c != math.pi:
            return False

        kut_b = Vektor.from_tocke(self.b, self.a).angle_with(Vektor.from_tocke(self.b, self.c))
        kut_d = Vektor.from_tocke(self.d, self.a).angle_with(Vektor.from_tocke(self.d, self.c))

        if kut_b + kut_d != math.pi:
            return False

        return True

    def jel_tangencijalni(self):
        if (Vektor.from_tocke(self.a, self.b).length() + Vektor.from_tocke(self.d, self.c).length()) == \
                (Vektor.from_tocke(self.a, self.d).length() + Vektor.from_tocke(self.b, self.c).length()):
            return True
        else:
            return False
