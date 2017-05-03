from _Duzina import Duzina
from _Tocka import Tocka

unosGreske = True

while(unosGreske):
    unosGreske = False
    input_a = None
    input_b = None
    input_c = None
    input_d = None
    print("")

    input_a = input("Unesite koordinate tocake A: ")
    input_b = input("Unesite koordinate tocake B: ")
    input_c = input("Unesite koordinate tocake C: ")
    input_d = input("Unesite koordinate tocake D: ")

    input_a = input_a.replace("(","").replace(")","").replace(","," ").replace("  ", " ")
    input_a = input_a.split(" ")

    input_b = input_b.replace("(","").replace(")","").replace(","," ").replace("  ", " ")
    input_b = input_b.split(" ")

    input_c = input_c.replace("(","").replace(")","").replace(","," ").replace("  ", " ")
    input_c = input_c.split(" ")

    input_d = input_d.replace("(","").replace(")","").replace(","," ").replace("  ", " ")
    input_d = input_d.split(" ")

    try:
        input_a = list(map(lambda x: float(x), input_a))
        input_b = list(map(lambda x: float(x), input_b))
        input_c = list(map(lambda x: float(x), input_c))
        input_d = list(map(lambda x: float(x), input_d))

        if len(input_a) < 2 or len(input_b) < 2 or len(input_c) < 2 or len(input_d) < 2:
            unosGreske = True
            print("Premali broj argumenata za tocku")

    except ValueError:
        print("Greska nije unesen broj")
        unosGreske = True

    if len(input_a) == 2:
        input_a.append(0)
    if len(input_b) == 2:
        input_b.append(0)
    if len(input_c) == 2:
        input_c.append(0)
    if len(input_d) == 2:
        input_d.append(0)

ab = Duzina(Tocka(input_a[0], input_a[1], input_a[2]), Tocka(input_b[0], input_b[1], input_b[2]))
cd = Duzina(Tocka(input_c[0], input_c[1], input_c[2]), Tocka(input_d[0], input_d[1], input_d[2]))

s = ab.get_sjeciste_s_duzinom(cd)
if s is not None:
    print("Duzine AB", ab, "i CD", cd, "se sjeku u", s)
else:
    print("Duzine AB", ab, "i CD", cd, "se ne sjeku")
print("")
