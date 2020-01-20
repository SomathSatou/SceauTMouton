# coding=utf-8
import copy
import minizinc as mnz
class Gallon:
    def __init__(self,numero, taille, remplissage_inital):
        if remplissage_inital> taille:
            print("ATTENTION, REMPLISSAGE INITIAL > TAILLE !")
        self.taille = taille
        self.remplissage = remplissage_inital
        self.numero = numero
        self.taille_restante = taille-remplissage_inital

    def __str__(self):
        return "\tGallon " + str(self.numero) + " taille " + str(self.taille) + " rempli a "+ str(self.remplissage)+"\n"

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
    def __init__(self, quantite_objectif, liste_gallons):

        # Create a MiniZinc model
        self.model = mnz.Model()
        self.model.add_file("ProjSceau.mzn")

        # Transform Model into a instance
        gecode = mnz.Solver.lookup("gecode")
        self.inst = mnz.Instance(gecode, self.model)

        self.gallons = liste_gallons
        self.quantite_objectif = quantite_objectif



        self.inst["nbr_sceau"] = len(liste_gallons)
        self.inst["remplissage_final"] = quantite_objectif

        list_taille_sceau = []
        list_remplissage_init = []
        for g in self.gallons:
            list_taille_sceau.append(g.taille)
            list_remplissage_init.append(g.remplissage)

        self.inst["taille_sceau"] = list_taille_sceau
        self.inst["remplissage_initial"] = list_remplissage_init


        print("CONFIGURATION d'ORIGINE:")
        print("\tnombre sceaux : ", self.inst["nbr_sceau"])
        print("\tremplissage_final : ", self.inst["remplissage_final"])
        print("\ttaille_sceau : ", self.inst["taille_sceau"])
        print("\tremplissage_initial : ", self.inst["remplissage_initial"])


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
        if len(result)==0:
            print("PAS DE SOLUTION")
            return False
        else:
            for i in range(len(result)):
                #print(result["remplissage"])
                #print(result["unsolved_step"])

                index = 0
                while result["unsolved_step"][index]==1:
                    index+=1

                gallon_number=0
                for g in self.gallons:
                    g.remplissage = result["remplissage"][index][gallon_number]
                    gallon_number+=1

                print("\nSOLUTION : ")
                print(self.gallons)
                return True


