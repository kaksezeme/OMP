from _Cetverokut import Cetverokut
from _Tocka import Tocka
from _Utils import *

def koja_vrsta(klasifikacija):
    if klasifikacija.__contains__("Romb"):
        return "Romb"
    if klasifikacija.__contains__("Kvadrat"):
        return "Kvadrat"
    if klasifikacija.__contains__("Paralelogram"):
        return "Paralelogram"
    if klasifikacija.__contains__("Pravokutnik"):
        return "Pravokutnik"
    if klasifikacija.__contains__("Deltoid"):
        return "Deltoid"
    if klasifikacija.__contains__("Trapez"):
        return "Trapez"

    vrsta = ""
    if len(klasifikacija) <= 2:
        for x in klasifikacija:
            vrsta = vrsta + " " + x
        return vrsta

tocke = get_input_arrays("ulaz.dat")
cetverokuti = []
for kordinata in tocke:
    cetverokuti.append(Cetverokut(Tocka(kordinata[0], kordinata[1]),
                                  Tocka(kordinata[2], kordinata[3]),
                                  Tocka(kordinata[4], kordinata[5]),
                                  Tocka(kordinata[6], kordinata[7])))
print("")

for cetverokut in cetverokuti:
    klasifikacije = cetverokut.klasifikacija()
    print(klasifikacije, "->", koja_vrsta(klasifikacije))

print("")