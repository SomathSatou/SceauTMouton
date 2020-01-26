from functools import partial
from tkinter import *

import Seau
import Mouton


def mainwindow():
    fenetre = Tk()

    fenetre.title('SeauTMouton')
    fenetre.geometry('700x350')
    center(fenetre)

    fenetre.rowconfigure(0, weight=1)
    fenetre.rowconfigure(1, weight=1)
    fenetre.rowconfigure(2, weight=1)
    fenetre.columnconfigure(0, weight=1)

    button_seau = Button(text="Seau", command=partial(seau_button, fenetre))
    button_mouton = Button(text="Saut Mouton", command=partial(mouton_button, fenetre))
    button_exit = Button(text="Exit", command=exit_button)

    button_seau.grid(row=0,column=0)
    button_mouton.grid(row=1,column=0)
    button_exit.grid(row=2,column=0)

    fenetre.mainloop()
    return


def exit_button():
    exit()
    return


def mouton_button(fenetre):
    fenetre.destroy()
    Mouton.parametreMouton()
    return


def seau_button(fenetre):
    fenetre.destroy()
    Seau.parametreSeau()
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