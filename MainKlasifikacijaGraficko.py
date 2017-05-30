from tkinter import *

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


def klasifikacija_button_click():
    tocke = get_input_arrays(putanja_textbox.get())
    cetverokuti = []
    for kordinata in tocke:
        cetverokuti.append(Cetverokut(Tocka(kordinata[0], kordinata[1]),
                                      Tocka(kordinata[2], kordinata[3]),
                                      Tocka(kordinata[4], kordinata[5]),
                                      Tocka(kordinata[6], kordinata[7])))
    index = 0
    list_box.delete(0, END)
    for cetverokut in cetverokuti:
        ispis = ""
        klasifikacije = cetverokut.klasifikacija()
        for klasa in klasifikacije:
            ispis = ispis + klasa + ", "
        ispis = ispis[:-2]
        list_box.insert(index, "Klasifikacija " + str(index+1) + ". četverokuta: "
                        + ispis + "; Vrsta: " + koja_vrsta(klasifikacije))
        index = index + 1

root = Tk()
root.minsize(800, 560)
root.wm_title('Klasifikacija četverokuta')

ftop = Frame(root)
ftop.pack(side=TOP, fill=X)

putanja_textbox = Entry(ftop)
putanja_textbox.pack(side=LEFT, fill=Y)
putanja_textbox.insert(0, "ulaz.dat")
klasifikacija_button = Button(ftop, text="Klasificiraj", command=klasifikacija_button_click)
klasifikacija_button.pack(side=LEFT)

list_box = Listbox(root, height=35)
list_box.pack(side=TOP, fill=BOTH)

root.mainloop()
