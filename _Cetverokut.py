from _Vektor import *

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
        ab = Vektor(self.A, self.B)
        bc = Vektor(self.B, self.C)
        cd = Vektor(self.C, self.D)
        da = Vektor(self.D, self.A)

        if ab.length() == cd.length() and bc.length() == da.length() and ab.angle_with(bc) == math.pi / 2:
            return True
        else:
            return False

    def jel_paralelogram(self):
        ab = Vektor(self.A, self.B)
        dc = Vektor(self.D, self.C)
        ad = Vektor(self.A, self.D)
        bc = Vektor(self.B, self.C)

        if ab == dc and ad == bc and ab.angle_with(bc) != math.pi / 2:
            return True
        else:
            return False


    def jel_konveksni(self):
        v1 = Vektor(self.A, self.B)
        v2 = Vektor(self.A, self.D)
        v3 = Vektor(self.B, self.A)
        v4 = Vektor(self.B, self.C)
        v5 = Vektor(self.C, self.B)
        v6 = Vektor(self.C, self.D)
        v7 = Vektor(self.D, self.C)
        v8 = Vektor(self.D, self.A)
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
        ab = Vektor(self.A, self.B)
        dc = Vektor(self.D, self.C)
        ad = Vektor(self.A, self.D)
        bc = Vektor(self.B, self.C)
        sjeciste_dijagonala = self.A.mid(self.C)

        v5 = Vektor(sjeciste_dijagonala, self.A)
        v6 = Vektor(sjeciste_dijagonala, self.D)

        dijagonala1 = Vektor(self.A, self.C)
        dijagonala2 = Vektor(self.B, self.D)

        if ab == dc and ad == bc and ab.length() == ad.length() and v5.angle_with(v6) == math.pi / 2 \
                and dijagonala1.length() != dijagonala2.length():
            return True
        else:
            return False

    def jeli_kvadrat(self):
        ba = Vektor(self.B, self.A)
        cd = Vektor(self.C, self.D)
        bc = Vektor(self.B, self.C)
        ac = Vektor(self.A, self.C)

        dijagonala = ba.length() * math.sqrt(2)

        if ba == cd and ba.angle_with(bc) == math.pi/2 and dijagonala == ac.length():
            return True
        else:
            return False


    def jel_tetivni(self):
        kut_a = Vektor(self.A, self.B).angle_with(Vektor(self.A, self.D))
        kut_c = Vektor(self.C, self.B).angle_with(Vektor(self.C, self.D))

        if kut_a + kut_c != math.pi:
            return False

        kut_b = Vektor(self.B, self.A).angle_with(Vektor(self.B, self.C))
        kut_d = Vektor(self.D, self.A).angle_with(Vektor(self.D, self.C))

        if kut_b + kut_d != math.pi:
            return False

        return True

    def jel_tangencijalni(self):
        if (Vektor(self.A, self.B).length() + Vektor(self.D, self.C).length()) == \
                (Vektor(self.A, self.D).length() + Vektor(self.B, self.C).length()):
            return True
        else:
            return False
