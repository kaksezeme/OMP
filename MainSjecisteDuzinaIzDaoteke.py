from _Duzina import Duzina
from _Utils import *


tocke = get_input_arrays("ulazDuzine.dat")
print("")
for t in tocke:
    ab = Duzina.from_list(t[:4])
    cd = Duzina.from_list(t[4:])

    s = ab.get_sjeciste_s_duzinom(cd)
    if s is not None:
        print("Duzine AB", ab, "i CD", cd, "\tse sjeku u", s)
    else:
        print("Duzine AB", ab, "i CD", cd, "\tse ne sjeku")
print("")