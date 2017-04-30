import math


class Vektor:

    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        """
        :param x: komponenta x trenutnog vektora 
        :param y: komponenta y trenutnog vektora
        :param z: komponenta zq trenutnog vektora
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        :return: string: ispis trenutnog vektora u kordinatama [x, y, z] 
        """
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

    @classmethod
    def from_tocke(cls, r1, r2):
        """
        :param r1: Radij vektor 1 
        :param r2: Radij vektor 2
        :return: Vektor (x, y, z)
        """
        x = r2.x - r1.x
        y = r2.y - r1.y
        z = r2.z - r1.z
        return cls(x, y, z)

    def length(self):
        """:return: float - duljina trenutnog vektora"""
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def scalar_with(self, v2):
        """
        :param v2: drugi vektor skalarnog produkta
        :return: float - skalarni produkt
        """
        return self.x * v2.x + self.y * v2.y + self.z * v2.z

    def vector_product(self, v2):
        """
        :param v2: drugi vektor vektorskog produkta
        :return: Vektor, rjesenje vektorskog produkta trenutnog vektora i vektora v2 
        """
        return Vektor((self.y * v2.z - self.z * v2.y), (self.z * v2.x - self.x * v2.z), (self.x * v2.y - self.y * v2.x))

    def paralel_with(self, v2):
        """
        :param v2: drugi vektor za provjeru paralelnosti 
        :return: bool: True vektori su paralelni; False vektori nisu paralelni
        """
        if self.vector_product(v2).length() == 0:
            return True
        else:
            return False

    def angle_with(self, v2):
        """
        :param v2: drugi vektor za odredivanje kuta 
        :return: float kut izmedu trenutnog vektora i vektora v2
        """
        scalar = self.scalar_with(v2)
        lengths = self.length() * v2.length()
        return math.acos(scalar/lengths)

    def __eq__(self, v2):
        """
        :param v2: drugi vektor s kojim se provjera jednakost
        :return: bool: True: dva vektora su jednaka; False: dva vektora nisu jednaka 
        """
        if self.x == v2.x and self.y == v2.y and self.z == v2.z:
            return True
        else:
            return False
