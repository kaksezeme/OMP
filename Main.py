from _Cetverokut import Cetverokut
from _Tocka import Tocka
from _Utils import *


tocke = get_input_arrays("ulaz.dat")
cetverokuti = []
for kordinata in tocke:
    cetverokuti.append(Cetverokut(Tocka(kordinata[0], kordinata[1]),
                                  Tocka(kordinata[2], kordinata[3]),
                                  Tocka(kordinata[4], kordinata[5]),
                                  Tocka(kordinata[6], kordinata[7])))


for cetverokut in cetverokuti:
    print(cetverokut)