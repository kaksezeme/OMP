from _Duzina import Duzina
from _Tocka import Tocka
#(1,1) (3,1) (4,4) (2,4)
a = Duzina(Tocka(0, 5), Tocka(3, 0))
b = Duzina(Tocka(0, 2), Tocka(3, 2))


s = a.get_sjeciste(b)
if (s != None):
    print("Sjeku se u ", s)
else:
    print("Ne sjeku se")
