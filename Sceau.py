from tkinter import *
from functools import partial

import Mainwindow


class SceauWindow:
    def __init__(self, nbrSceau, tailles, final, initial):
        self._contenu = []
        self._first = True
        self._select = -1
        self._tailles = tailles
        self.Sceau_w = ""
        self._final = final
        self._initial = initial
        self.nbrSceau = nbrSceau
        self.update_list=[]

        for i in range(0, nbrSceau):
            self._contenu.append(initial[i] * tailles[i])
        self.launch()

    def launch(self):
        self.Sceau_w = Tk()
        self.Sceau_w.title('Jeu des Sceaux')
        self.Sceau_w.geometry('1200x350')
        self.center(self.Sceau_w)

        photo = PhotoImage(file='img/sceau.gif')

        for i in range(1, self.nbrSceau + 1):
            self.Sceau_w.columnconfigure(i, weight=1)
            Button(image=photo, command=partial(self.vide, i - 1)).grid(row=0, column=i)

        self.Sceau_w.rowconfigure(0, weight=1)
        self.Sceau_w.rowconfigure(1, weight=1)
        self.Sceau_w.rowconfigure(2, weight=1)

        for i in range(0, self.nbrSceau):
            self.update_list.append(StringVar())
            lab = Label(textvariable=self.update_list[i], relief=RAISED).grid(row=1, column=i + 1)
            self.update_list[i].set(str(self._contenu[i]) + "/" + str(self._tailles[i]))

        button_retour = Button(text="Retour", command=self.retour_button)
        button_retour.grid(row=2, column=self.nbrSceau)
        self.Sceau_w.mainloop()
        return

    def retour_button(self):
        self.Sceau_w.destroy()
        self._contenu = []
        Mainwindow.mainwindow()
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

    def vide(self, indice):
        if self._first:
            self._select = indice
            self._first = False
        else:
            if indice != self._select:
                reste = self._tailles[indice] - (self._contenu[indice] + self._contenu[self._select])
                if reste >= 0:
                    self._contenu[indice] = self._contenu[indice] + self._contenu[self._select]
                    self._contenu[self._select] = 0
                else:
                    self._contenu[indice] = self._tailles[indice]
                    self._contenu[self._select] = -reste
                self._first = True
            print(self._contenu)
            for i in range(0, self.nbrSceau):
                self.update_list[i].set(str(self._contenu[i]) + "/" + str(self._tailles[i]))

        return


class parametreSceau:
    def __init__(self):
        # reste a faire la fenetre pour les paramètre
        return