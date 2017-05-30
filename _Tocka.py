class Tocka:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z=0.0):
        """
        :param x: komponenta x trenutne tocke 
        :param y: komponenta y trenutne tocke
        :param z: komponenta z trenutne tocke. Podrazumjevana vrijednost je postavljena na 0
        """
        self.x = x
        self.y = y
        self.z = z

    def mid(self, t2):
        """
        :param t2: druga tocka 
        :return: Tocka predstavlja poloviste izmedu dvije tocke
        """
        x_mid = (self.x + t2.x) / 2
        y_mid = (self.y + t2.y) / 2
        z_mid = (self.z + t2.z) / 2
        return Tocka(x_mid, y_mid, z_mid)

    def __eq__(self, other):
        """
        :param other: druga tocka 
        :return: bool: True - dvije točke su iste; False - dvije točke nisu iste
        """
        if other is None:
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        """
        :return: string - ispis trenutne tocke u kordinatama (x, y, z) 
        """
        return "(" + str(self.x) + ", " + str(self.y) + ")"
