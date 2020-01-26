from tkinter import *
from functools import partial

import Mainwindow


class MoutonWindow:
    def __init__(self, nbrMouton):
        self.nbrMouton = nbrMouton
        self.size_w = str((240*nbrMouton)*2+240) + 'x350'
        self.Mouton_w = ""
        self.moutons = []
        self.launch()

        return

    def launch(self):
        self.Mouton_w = Tk()
        self.Mouton_w.title('Jeu des Moutons')
        self.Mouton_w.geometry(self.size_w)
        self.center()

        blanc = PhotoImage(file='img/mouton/white.png')
        noir = PhotoImage(file='img/mouton/black.png')

        for i in range(0, self.nbrMouton):
            self.Mouton_w.columnconfigure(i, weight=1)
            Button(image=blanc, command=partial(self.moove, i)).grid(row=0, column=i)
            self.moutons.append(-1)

        self.Mouton_w.columnconfigure(self.nbrMouton+1, weight=1)
        Button(width=24, height=22, command=partial(self.moove, i)).grid(row=0, column=self.nbrMouton+1)
        self.moutons.append(0)

        for i in range(self.nbrMouton+2, self.nbrMouton+2+self.nbrMouton):
            self.Mouton_w.columnconfigure(i, weight=1)
            Button(image=noir, command=partial(self.moove, i)).grid(row=0, column=i)
            self.moutons.append(1)

        self.Mouton_w.rowconfigure(0, weight=1)
        self.Mouton_w.rowconfigure(1, weight=1)

        button_retour = Button(text="Retour", command=self.retour_button)
        button_retour.pack(side=LEFT)
        self.Mouton_w.mainloop()
        return

    def retour_button(self):
        self.Mouton_w.destroy()
        Mainwindow.mainwindow()
        return

    def moove(self, indice):

        return

    def center(self):
        self.Mouton_w.update_idletasks()

        # Tkinter way to find the screen resolution
        screen_width = self.Mouton_w.winfo_screenwidth()
        screen_height = self.Mouton_w.winfo_screenheight()

        size = tuple(int(_) for _ in self.Mouton_w.geometry().split('+')[0].split('x'))
        x = screen_width / 2 - size[0] / 2
        y = screen_height / 2 - size[1] / 2

        self.Mouton_w.geometry("+%d+%d" % (x, y))
        return


class parametreMouton:
    def __init__(self):
        # reste a faire la fenetre pour les paramètre
        self.parametre = Tk()
        self.parametre.title('Jeu des Moutons')
        self.parametre.geometry('700x350')
        self.center(self.parametre)

        self.parametre.columnconfigure(0, weight=1)
        self.parametre.columnconfigure(1, weight=1)
        self.parametre.rowconfigure(0, weight=1)
        self.parametre.rowconfigure(1, weight=1)

        self.nbrMouton = 3

        button_retour = Button(text="Valider", command=self.check_button, width=10)
        button_retour.grid(row=1, column=1)

        Label(text="Nombre de mouton :").grid(row=0, column=0)

        self.entry_nbrM = StringVar()
        Entry(textvariable=self.entry_nbrM, width=40).grid(row=0, column=1)
        self.entry_nbrM.set("3")
        return

    def check_button(self):
        self.parametre.destroy()

        self.nbrMouton = int(self.entry_nbrM.get())

        if self.check():
            MoutonWindow(self.nbrMouton)
        else:
            # pop-up mauvais argument
            parametreMouton()
        return

    def center(self, toplevel):
        toplevel.update_idletasks()

        # Tkinter way to find the screen resolution
        screen_width = toplevel.winfo_screenwidth()
        screen_height = toplevel.winfo_screenheight()

        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = screen_width / 2 - size[0] / 2
        y = screen_height / 2 - size[1] / 2

        toplevel.geometry("+%d+%d" % (x, y))
        return

    def check(self):
        #return model.solve()
        return True
