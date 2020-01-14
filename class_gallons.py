class Gallon:
    def __init__(self,numero, taille):
        self.taille = taille
        self.remplissage = 0
        self.numero = numero
        self.taille_restante = taille

    def __str__(self):
        return "Gallon " + str(self.numero) + " taille " + str(self.taille) + " rempli a "+ str(self.remplissage)

    def __repr__(self):
        return self.__str__()


    def remplir(self, nombre):
        if nombre<=self.taille_restante:
            self.remplissage+=nombre
            self.taille_restante-=nombre
        else:
            self.remplissage=self.taille
            self.taille_restante-=nombre
           print("Attention, le gallon ", str(self.numero), " est déjà plein ")
        

class Liste_Gallon:
    def __init__(self):
        self.gallons = []

    def __str__(self):
        return str(self.gallons)
    def __repr__(self):
        return self.__str__()

    def append(self, gallon):
        self.gallons.append(gallon)