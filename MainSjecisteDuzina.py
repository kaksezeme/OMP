from _Duzina import Duzina
from _Tocka import Tocka

a = Duzina(Tocka(3, 3), Tocka(1, 1))
b = Duzina(Tocka(4, 2), Tocka(-2, 6))


s = a.get_sjeciste(b)
if (s != None):
    print("Sjeku se u ", s)
else:
    print("Ne sjeku se")
