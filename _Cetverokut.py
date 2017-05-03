from _Vektor import *
from _Duzina import *


class Cetverokut:
    """
    Predstavlja četverokut ABCD za koji treba odrediti klasifikaciju
    """
    a = None
    b = None
    c = None
    d = None

    def __init__(self, a, b, c, d):
        """
        :param a: Tocka A cetverokuta 
        :param b: Tocka B cetverokuta
        :param c: Tocka C cetverokuta
        :param d: Tocka D cetverokuta
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        """
        :return: string - ispis cetverokuta preko kooridnata tocaka 
        """
        return "A" + str(self.a) + " B" + str(self.b) + " C" + str(self.c) + " D" + str(self.d)

    def postoje_iste_tocke(self):
        """
        Provjerava je li jedna od tocaka (A, B, C, D) jednaka drugoj.
        :return:  bool: True tocka je jednaka nekoj drugoj tocki cetverokuta; False sve tocke su razlicite
        """
        return self.a == self.b or self.a == self.c \
               or self.a == self.d or self.b == self.c \
               or self.b == self.d or self.c == self.d

    def klasifikacija(self):
        """
        Prolazi kroz sve tipove cetverokuta te provjerava je li trenutni cetverokut odredenog tipa. Tip cetverokuta
        koji pripada trenutnom cetverokutu dodaje u listu tipova.
        :return: list sve vrste cetverokuta kojima spada trenutni cetverokut na temelju klasifikacije
        """
        if self.postoje_iste_tocke():
            return ["Cetverokut nema 4 razlicite tocke"]

        tipovi = []

        try:

            if self.jel_konveksni():
                tipovi.append("Konveksni")
            else:
                tipovi.append("Konkavni")

            if self.jel_slozen():
                tipovi.append("Slozeni")
            else:
                tipovi.append("Jednostavan")
                if self.jel_deltoid():
                    tipovi.append("Deltoid")
                if self.jel_trapez():
                    tipovi.append("Trapez")
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
        except ValueError:
            return ["Neispravan cetverokut"]
        return tipovi

    def jel_deltoid(self):
        """
        Provjerava je li trenutni cetverokut deltoid. Prvo provjerava je li tangencijalni. Ako nije, nije ni deltoid.
        Pronalazi sjeciste dijagonala, kut izmedu njih mora biti 90 stupnjeva. Provjerava jesu li susjedne stranice
        cetverokuta jednake duljine.
        :return: bool: True - cetverokut je deltoid; False - cetverokut nije deltoid  
        """
        if self.jel_tangencijalni() is not True:
            return False

        d_ac = Duzina(self.a, self.c)
        d_bd = Duzina(self.b, self.d)

        sjeciste_dijagonala = d_ac.get_sjeciste_s_duzinom(d_bd)

        v1 = Vektor.from_tocke(sjeciste_dijagonala, self.a)
        v2 = Vektor.from_tocke(sjeciste_dijagonala, self.b)

        if round(v1.angle_with(v2), 5) != round(math.pi / 2, 5):
            return False

        if d_ac.length() > d_bd.length():
            v_ab = Vektor.from_tocke(self.a, self.b)
            v_ad = Vektor.from_tocke(self.a, self.d)
            v_cb = Vektor.from_tocke(self.c, self.b)
            v_cd = Vektor.from_tocke(self.c, self.d)

            if v_ab.length() == v_ad.length() and v_cb.length() == v_cd.length():
                return True
        else:
            v_da = Vektor.from_tocke(self.d, self.a)
            v_dc = Vektor.from_tocke(self.d, self.c)
            v_ba = Vektor.from_tocke(self.b, self.a)
            v_bc = Vektor.from_tocke(self.b, self.c)

            if v_da.length() == v_dc.length() and v_ba.length() == v_bc.length():
                return True

        return False

    def jel_trapez(self):
        """
        Provjerava je li trenutni cetverokut trapez. Provjerava je li vektor ab paralelan s dc. Ako su ta dva vektora
        paralelna onda vektori ad i bc ne smiju biti paralelni. Drugi moguci slucaj je da su vektori ad i bc paraleni.
        Tada vektori ab i dc ne smiju biti paralelni.
        :return:  bool: True - cetverokut je trapez; False - cetverokut nije trapez
        """
        ab = Vektor.from_tocke(self.a, self.b)
        dc = Vektor.from_tocke(self.d, self.c)
        ad = Vektor.from_tocke(self.a, self.d)
        bc = Vektor.from_tocke(self.b, self.c)

        if ab.paralel_with(dc) and ad.paralel_with(bc) is False:
            return True

        if ad.paralel_with(bc) and ab.paralel_with(dc) is False:
            return True

        return False

    def jel_slozen(self):
        """
        Provjerava je li trenutni cetverokut slozen. Provjerava postoji li sjeciste duzina ab i dc ili ad i bc.
        Ako jedno od sjecista postoji, cetverokut je slozen.
        :return: bool: True - cetverokut je slozen; False - cetverokut nije slozen 
        """
        ab = Duzina(self.a, self.b)
        dc = Duzina(self.d, self.c)
        ad = Duzina(self.a, self.d)
        bc = Duzina(self.b, self.c)

        if ab.get_sjeciste_s_duzinom(dc) is not None or ad.get_sjeciste_s_duzinom(bc) is not None:
            return True
        else:
            return False

    def jel_jednostavan(self):
        """
        Provjerava je li trenutni cetverokut jednostavan. Ako nije složen tada je jednostavan.
        :return: bool: True - cetverokut je jednostavan; False - cetverokut nije jednostavan
        """
        if self.jel_slozen():
            return False
        else:
            return True

    def jel_pravokutnik(self):
        """
        Provjerava je li trenutni cetverokut pravokutnik. Ako su duzine ab i cd tada i duzine bc i da moraju biti
        iste duzine. Također, kut izmedu ab i bc mora biti 90 stupnjeva.
        :return: bool: True - cetverokut je pravokutnik; False - cetverokut nije pravokutnik
        """
        ab = Vektor.from_tocke(self.a, self.b)
        bc = Vektor.from_tocke(self.b, self.c)
        cd = Vektor.from_tocke(self.c, self.d)
        da = Vektor.from_tocke(self.d, self.a)

        if ab.length() == cd.length() and bc.length() == da.length() and ab.angle_with(bc) == math.pi / 2:
            return True
        else:
            return False

    def jel_paralelogram(self):
        """
        Provjerava je li trenutni cetverokut paralelogram. Cetverokut je paralelogram ako su vekotir ab i dc jednaki.
        Odnosno ako su vektori ad i bc jednaki. Također, kut između susjednih stranica ne smije biti 90 stupnjeva.
        :return: bool: True - cetverokut je paralelogram; False - cetverokut nije paralelogram
        """
        ab = Vektor.from_tocke(self.a, self.b)
        dc = Vektor.from_tocke(self.d, self.c)
        ad = Vektor.from_tocke(self.a, self.d)
        bc = Vektor.from_tocke(self.b, self.c)

        if ab == dc and ad == bc and ab.angle_with(bc) != math.pi / 2:
            return True
        else:
            return False

    def jel_konveksni(self):
        """
        Provjerava je li trenutni cetverokut konveksni. Svaki unutarnji kut mora biti manji od 180 stupnjeva.
        Odnosno, zbroj svih unutarnjih kuteva mora biti 360 stupnjeva.
        :return: bool: True - cetverokut je konveksni; False - cetverokut nije konveksni
        """
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
        """
        Provjerava je li trenutni cetverokut konkavni. Ako cetverokut nije konveksni tada je konkavni
        :return: bool: True - cetverokut je konkavni; False - cetverokut nije konkavni 
        """
        if self.jel_konveksni():
            return False
        else:
            return True

    def jel_romb(self):
        """
        Provjerava je li trenutni cetverokut romb. duljine susjednih stranica mora biti jednake duljine, a dijagonale
        se sjeku pod 90 stupnjeva i nisu jednake duljine.
        :return: bool: True - cetverokut je romb; False - cetverokut nije romb
        """
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
        """
        Provjerava je li trenutni cetverokut kvadrat. Sve stranice su jednake duljine i kut izmedu susjednih stranica
        je 90 stupnjeva.
        :return: bool: True - cetverokut je kvadrat; False - cetverokut nije kvadrat
        """
        ba = Vektor.from_tocke(self.b, self.a)
        cd = Vektor.from_tocke(self.c, self.d)
        bc = Vektor.from_tocke(self.b, self.c)

        if ba.length() == cd.length() and ba.length() == bc.length() and ba.angle_with(bc) == math.pi/2:
            return True
        else:
            return False

    def jel_tetivni(self):
        """
        Provjerava je li trenutni cetverokut tetivni. Zbroj nasuprotnih kuteva mora biti 180 stupnjeva
        :return: bool: True - cetverokut je tetivni; False - cetverokut nije tetivni
        """
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
        """
        Provjerava je li trenutni cetverokut tangencijalni. Zbroj nasuprotnih strana mora biti jednake duljine.
        :return: bool: True - cetverokut je tangencijalni; False - cetverokut nije tangencijalni
        """
        if (Vektor.from_tocke(self.a, self.b).length() + Vektor.from_tocke(self.d, self.c).length()) == \
                (Vektor.from_tocke(self.a, self.d).length() + Vektor.from_tocke(self.b, self.c).length()):
            return True
        else:
            return False
