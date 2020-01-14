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


    def remplir(self, quantite_eau):
        if quantite_eau<=self.taille_restante:
            self.remplissage+=quantite_eau
            self.taille_restante-=quantite_eau
        else:
            self.remplissage=self.taille
            self.taille_restante-=quantite_eau
            print("Attention, le gallon ", str(self.numero), " est déjà plein ")

    def vider(self, quantite_eau):
        if quantite_eau>self.taille_restante:
            print("Le gallon ", str(self.numero), " est désormais vide")
            self.remplissage=0
            self.taille_restante=self.taille
        else:
            self.remplissage-=quantite_eau
            self.taille_restante+=quantite_eau
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

    def transfert(self, gallon_1, gallon_2, quantite_eau):
        gallon_1.remplir(quantite_eau)
        gallon_2.enlever(quantite_eau)