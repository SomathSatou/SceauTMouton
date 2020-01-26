from tkinter import *
from functools import partial

import Mainwindow


class MoutonWindow:
    def __init__(self, nbrMouton):
        self.nbrMouton = nbrMouton
        self.size_w = str((270*nbrMouton)*2+270) + 'x350'
        self.Mouton_w = ""
        self.moutons = []

        self.blanc = ""
        self.noir = ""
        self.vide = ""
        self.button_list = []

        self.launch()
        return

    def launch(self):
        self.Mouton_w = Tk()
        self.Mouton_w.title('Jeu des Moutons')
        self.Mouton_w.geometry(self.size_w)
        self.center()

        self.blanc = PhotoImage(file='img/mouton/white.png')
        self.noir = PhotoImage(file='img/mouton/black.png')
        self.vide = PhotoImage(file='img/mouton/vide.png')

        for i in range(0, self.nbrMouton):
            self.Mouton_w.columnconfigure(i, weight=1)
            tmp = Button(image=self.blanc, command=partial(self.moove, i))
            self.moutons.append(-1)
            self.button_list.append(tmp)
            self.button_list[i].grid(row=0, column=i)

        self.Mouton_w.columnconfigure(self.nbrMouton+1, weight=1)
        tmp = Button(image=self.vide, command=partial(self.moove, i))
        self.moutons.append(0)
        self.button_list.append(tmp)
        self.button_list[self.nbrMouton].grid(row=0, column=self.nbrMouton+1)

        for i in range(self.nbrMouton+1, self.nbrMouton+1+self.nbrMouton):
            self.Mouton_w.columnconfigure(i, weight=1)
            tmp = Button(image=self.noir, command=partial(self.moove, i))
            self.moutons.append(1)
            self.button_list.append(tmp)
            self.button_list[i].grid(row=0, column=i+1)

        self.Mouton_w.rowconfigure(0, weight=1)
        self.Mouton_w.rowconfigure(1, weight=1)

        button_retour = Button(text="Retour", command=self.retour_button)
        button_retour.grid(row=1, column=self.nbrMouton+2+self.nbrMouton-1)

        button_init = Button(text="Reinitialiser", command=self.init_button)
        button_init.grid(row=1, column=self.nbrMouton+2+self.nbrMouton-2)

        self.Mouton_w.mainloop()
        return

    def retour_button(self):
        self.Mouton_w.destroy()
        Mainwindow.mainwindow()
        return

    def init_button(self):
        self.moutons = []
        for i in range(0, self.nbrMouton):
            self.moutons.append(-1)
        self.moutons.append(0)
        for i in range(self.nbrMouton+1, self.nbrMouton+1+self.nbrMouton):
            self.moutons.append(1)
        print(self.moutons)
        self.draw()
        return

    def moove(self, i):
        if self.moutons[i] == 1:
            #procedure pour déplacer un mouton noir
            if (i-1 >= 0) & (self.moutons[i-1] == 0):
                self.moutons[i-1] = 1
                self.moutons[i] = 0
            elif (i-2 >= 0) & (self.moutons[i-2] == 0):
                self.moutons[i-2] = 1
                self.moutons[i] = 0
        elif self.moutons[i] == -1:
            #procedure pour mouton blanc
            if (i+1 <= len(self.moutons)) & (self.moutons[i+1] == 0):
                self.moutons[i+1] = -1
                self.moutons[i] = 0
            elif (i+2 <= len(self.moutons)) & (self.moutons[i+2] == 0):
                self.moutons[i+2] = -1
                self.moutons[i] = 0
        self.draw()
        return

    def draw(self):
        for i in range(len(self.moutons)):
            if self.moutons[i] == -1:
                self.button_list[i].configure(image=self.blanc, command=partial(self.moove, i))
            elif  self.moutons[i] == 1:
                self.button_list[i].configure(image=self.noir, command=partial(self.moove, i))
            elif self.moutons[i] == 0:
                self.button_list[i].configure(image=self.vide, command=partial(self.moove, i))
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
