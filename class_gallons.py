# coding=utf-8
import copy
import minizinc as mnz
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
        #if quantite_eau<=self.taille_restante:
        self.remplissage+=quantite_eau
        self.taille_restante-=quantite_eau
        #else:
        #    self.remplissage=self.taille
        #    self.taille_restante-=quantite_eau
        #    print("Attention, le gallon ", str(self.numero), " est déjà plein ")

    def remplir_completement(self):

        self.remplissage = self.taille
        self.taille_restante=0

    def enlever(self, quantite_eau):
        #if quantite_eau>self.taille_restante:
            #print("Le gallon ", str(self.numero), " est désormais vide")
        self.remplissage-=quantite_eau
        self.taille_restante+=quantite_eau
        #else:
        #    self.remplissage-=quantite_eau
        #    self.taille_restante+=quantite_eau
        #    print("Attention, le gallon ", str(self.numero), " est déjà plein ")


class Modelisation_Gallon:
    def __init__(self, quantite_initiale, quantite_objectif, liste_gallons):

        # Create a MiniZinc model
        self.model = mnz.Model()
        self.model.add_file("ProjSceau.mzn")

        # Transform Model into a instance
        gecode = mnz.Solver.lookup("gecode")
        self.inst = mnz.Instance(gecode, self.model)

        self.gallons = liste_gallons
        self.quantite_initiale = quantite_initiale
        self.quantite_objectif = quantite_objectif


        quantite_initiale_copy = copy.deepcopy(quantite_initiale)
        while quantite_initiale_copy >0:
            for g in self.gallons:
                if g.taille_restante>=1 and quantite_initiale_copy>0:
                    g.remplir(1)
                    quantite_initiale_copy-=1

        if quantite_initiale_copy>0:
            print("Impossible de remplir tout les gallons avec de l'eau. Veuillez augmenter la taille des gallons ou mettre moins d'eau")


        self.inst["nbr_sceau"] = len(liste_gallons)
        self.inst["remplissage_final"] = quantite_objectif
        self.inst["taille_sceau"] = { x.taille for x in liste_gallons}
        self.inst["remplissage_initial"] = {x.remplissage for x in liste_gallons}

    def __str__(self):
        return str(self.gallons)
    def __repr__(self):
        return self.__str__()

    def ajouter_un_gallon(self, gallon):
        self.gallons.append(gallon)

    def transfert(self, gallon_1, gallon_2):
        """Transfert le contenu du gallon 1 dans le 2. Si gallon 1 > gallon 2 alors le gallon garde le reste"""


        if gallon_1.remplissage<=0:
            return "Impossible de remplir, le gallon 1 est vide"


        elif gallon_2.taille_restante>=gallon_1.remplissage:
            gallon_2.remplir(gallon_1.remplissage)
            gallon_1.enlever(gallon_1.remplissage) #VIDER

        elif gallon_2.taille_restante<gallon_1.remplissage:
            copy_gallon_2_taille_restante = copy.deepcopy(gallon_2.taille_restante)
            gallon_2.remplir_completement()
            gallon_1.enlever(copy_gallon_2_taille_restante)


    def check_solution(self):
        for g in self.gallons:
            if g.remplissage == self.quantite_objectif:
                return True
        return False


    def solve(self):
        # Solve the instance
        result = self.inst.solve(all_solutions=False)
        for i in range(len(result)):
            print(result["remplissage"])
            print(result["unsolved_step"])

