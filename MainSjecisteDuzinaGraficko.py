from tkinter import *
from tkinter import messagebox
from _Duzina import Duzina
from _Tocka import Tocka

def submit_button_click():
    try:

        ab = Duzina(Tocka(float(t1x.get()), float(t1y.get())), Tocka(float(t2x.get()), float(t2y.get())))
        cd = Duzina(Tocka(float(t3x.get()), float(t3y.get())), Tocka(float(t4x.get()), float(t4y.get())))
        msg = ""

        s = ab.get_sjeciste_s_duzinom(cd)
        if s is not None:
            msg = "Duzine T1T2 i T3T4" + " se sjeku u (" + str(round(s.x,2)) + "," + str(round(s.y,2)) + ")"
        else:
            msg = "Duzine T1T2 i T3T4" + " se ne sjeku"

        messagebox.showinfo("Poruka", msg)
    except ValueError:
        messagebox.showerror("Greška", "Nisu uneseni brojevi")





root = Tk()
root.resizable(width=False, height=False)
root.minsize(300,150);
root.wm_title('Sjecište dužina')

space_textboxs = 20
textbox_width = 10
label_width = 5

ftop = Frame(root,height=40)
ftop.pack(side=TOP)

lblx = Label(ftop,text="x")
lblx.pack(side=LEFT, padx=60)

lblx = Label(ftop,text="y")
lblx.pack(side=LEFT)

f1 = Frame(root)
f1.pack(side=TOP)
lblT1 = Label(f1, text="T1", width=label_width)
lblT1.pack(side=LEFT)
t1x = Entry(f1, width=textbox_width)
t1x.pack(side=LEFT)
f1space = Frame(f1, width=space_textboxs)
f1space.pack(side=LEFT)
t1y = Entry(f1, width=textbox_width)
t1y.pack(side=LEFT)



f2 = Frame(root)
f2.pack(side=TOP)

lblT2 = Label(f2, text="T2", width=label_width)
lblT2.pack(side=LEFT)
t2x = Entry(f2, width=textbox_width)
t2x.pack(side=LEFT)
f2space = Frame(f2, width=space_textboxs)
f2space.pack(side=LEFT)
t2y = Entry(f2, width=textbox_width)
t2y.pack(side=LEFT)


f3 = Frame(root)
f3.pack(side=TOP)

lblT3 = Label(f3, text="T3", width=label_width)
lblT3.pack(side=LEFT)
t3x = Entry(f3, width=textbox_width)
t3x.pack(side=LEFT)
f3space = Frame(f3, width=space_textboxs)
f3space.pack(side=LEFT)
t3y = Entry(f3, width=textbox_width)
t3y.pack(side=LEFT)

f4 = Frame(root)
f4.pack(side=TOP)

lblT4 = Label(f4, text="T4", width=label_width)
lblT4.pack(side=LEFT)
t4x = Entry(f4, width=textbox_width)
t4x.pack(side=LEFT)
f4space = Frame(f4, width=space_textboxs)
f4space.pack(side=LEFT)
t4y = Entry(f4, width=textbox_width)
t4y.pack(side=LEFT)

f5 = Frame(root)
f5.pack(side=TOP)

bsubmit = Button(f5, text="Provjeri sjecište", command=submit_button_click)
bsubmit.pack(side=LEFT)


root.mainloop()