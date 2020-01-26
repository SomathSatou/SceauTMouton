from tkinter import *
from functools import partial

import Mainwindow
import class_gallons


class SeauWindow:
    def __init__(self, nbrSeau, tailles, final, initial):
        self._contenu = []
        self._first = True
        self._select = -1
        self._tailles = tailles
        self.Seau_w = ""
        self._final = final
        self._initial = initial
        self.nbrSeau = nbrSeau
        self.update_list=[]
        self.pop =""

        for i in range(0, nbrSeau):
            self._contenu.append(initial[i] * tailles[i])
        self.launch()

    def launch(self):
        self.Seau_w = Tk()
        self.Seau_w.title('Jeu des Seaux')
        self.Seau_w.geometry('1200x350')
        self.center(self.Seau_w)

        photo = PhotoImage(file='img/seau.gif')

        for i in range(1, self.nbrSeau + 1):
            self.Seau_w.columnconfigure(i, weight=1)
            Button(image=photo, command=partial(self.vide, i - 1)).grid(row=0, column=i)

        self.Seau_w.rowconfigure(0, weight=1)
        self.Seau_w.rowconfigure(1, weight=1)
        self.Seau_w.rowconfigure(2, weight=1)

        for i in range(0, self.nbrSeau):
            self.update_list.append(StringVar())
            labelfont = ('comic', 28, 'bold')
            lab = Label(textvariable=self.update_list[i], relief=RAISED, )
            lab.config(font=labelfont)
            lab.grid(row=1, column=i + 1)
            self.update_list[i].set(str(self._contenu[i]) + "/" + str(self._tailles[i]))

        button_retour = Button(text="Retour", command=self.retour_button)
        button_retour.grid(row=2, column=self.nbrSeau)
        self.Seau_w.mainloop()
        return

    def retour_button(self):
        self.Seau_w.destroy()
        self._contenu = []
        Mainwindow.mainwindow()
        return

    def retour_pop(self):
        self.pop.destroy()
        self.retour_button()
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
            for i in range(0, self.nbrSeau):
                self.update_list[i].set(str(self._contenu[i]) + "/" + str(self._tailles[i]))
            self.test()
        return

    def test(self):
        for i in range (0,self.nbrSeau):
            if self._contenu[i] == self._final:
                # lancer un self.popup
                self.pop = Tk()
                self.pop.title('Jeu des Seaux')
                self.pop.geometry('350x350')
                self.center(self.pop)

                self.pop.columnconfigure(0, weight=1)
                self.pop.rowconfigure(0, weight=1)
                self.pop.rowconfigure(1, weight=2)

                Label(self.pop, text="Vous avez gagné félicitation").grid(row=0, column=0)
                Button(self.pop, text="Exit", command=self.retour_pop).grid(row=1, column=0)
        return


class parametreSeau:
    def __init__(self):
        # reste a faire la fenetre pour les paramètre
        self.parametre = Tk()
        self.parametre.title('Jeu des Seaux')
        self.parametre.geometry('700x350')
        self.center(self.parametre)

        self.parametre.columnconfigure(0, weight=1)
        self.parametre.columnconfigure(1, weight=1)
        self.parametre.rowconfigure(0, weight=1)
        self.parametre.rowconfigure(1, weight=1)
        self.parametre.rowconfigure(2, weight=1)
        self.parametre.rowconfigure(3, weight=1)
        self.parametre.rowconfigure(4, weight=1)

        self.nbrSeau = 5
        self.tailles = [1, 2, 3, 4, 5]
        self.final = 4
        self.initial = [1, 1, 1, 1, 0]

        button_retour = Button(text="Valider", command=self.check_button, width=10)
        button_retour.grid(row=4, column=1)

        Label(text="Nombre de seau :").grid(row=0, column=0)
        Label(text="Tailles des seau (exemple pour 5 seau : 1;2;3;4;5) :").grid(row=1, column=0)
        Label(text="But a atteindre :").grid(row=2, column=0)
        Label(text="Remplissage initial (0 pour vide et 1 pour plein) :").grid(row=3, column=0)

        self.entry_nbrS = StringVar()
        Entry(textvariable=self.entry_nbrS, width=40).grid(row=0, column=2)
        self.entry_nbrS.set("5")

        self.entry_tailles = StringVar()
        Entry(textvariable=self.entry_tailles, width=40).grid(row=1, column=2)
        self.entry_tailles.set("1;2;3;4;5")

        self.entry_final = StringVar()
        Entry(textvariable=self.entry_final, width=40).grid(row=2, column=2)
        self.entry_final.set("4")

        self.entry_initial = StringVar()
        Entry(textvariable=self.entry_initial, width=40).grid(row=3, column=2)
        self.entry_initial.set("1;1;1;1;0")

        return

    def check_button(self):
        self.parametre.destroy()

        self.nbrSeau = int(self.entry_nbrS.get())

        tmp = self.entry_tailles.get().split(";")
        self.tailles = []
        for elt in tmp:
            self.tailles.append(int(elt))

        self.final = int(self.entry_final.get())

        tmp = self.entry_initial.get().split(";")
        self.initial = []
        for elt in tmp:
            self.initial.append(int(elt))

        if self.check() :
            SeauWindow(self.nbrSeau, self.tailles, self.final, self.initial)
        else :
            # pop-up mauvais argument
            parametreSeau()
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
        list_gallon = []
        for i in range(0, self.nbrSeau):
            list_gallon.append(
                class_gallons.Gallon(numero=i,
                                     taille=self.tailles[i-1],
                                     remplissage_inital=self.tailles[i-1]*self.initial[i-1])
            )

        model = class_gallons.Modelisation_Gallon(quantite_objectif=self.final, liste_gallons=list_gallon)
        return model.solve()
