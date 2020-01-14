from tkinter import *
from functools import partial

import Mainwindow


def SceauWindow():
    Sceau_w = Tk()
    Sceau_w.title('Jeu des Sceaux')
    Sceau_w.geometry('1200x350')
    center(Sceau_w)

    button_retour = Button(text="Retour", command=partial(retour_button, Sceau_w))
    button_retour.pack(side=LEFT)
    Sceau_w.mainloop()
    return


def retour_button(Sceau_w):
    Sceau_w.destroy()
    Mainwindow.mainwindow()
    return


def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    toplevel.geometry("+%d+%d" % (x, y))
    return
