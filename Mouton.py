from tkinter import *
from functools import partial

import Mainwindow

def MoutonWindow():
    Mouton_w = Tk()

    Mouton_w.title('Jeu des Sceaux')
    Mouton_w.geometry('1200x350')
    center(Mouton_w)

    button_retour = Button(text="Retour", command=partial(retour_button, Mouton_w))
    button_retour.pack(side=LEFT)
    Mouton_w.mainloop()
    return

def retour_button(Mouton_w):
    Mouton_w.destroy()
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
