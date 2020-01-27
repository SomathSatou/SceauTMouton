import minizinc as mnz


class Mouton:
    def __init__(self,numero, couleur):
        self.couleur = couleur
        self.numero = numero

    def __str__(self):
        return "\tMouton " + str(self.numero) + " couleur " + str(self.couleur) +"\n"

    def __repr__(self):

        return self.__str__()


class Modelisation_Mouton:
    def __init__(self, nombre_moutons):

        # Create a MiniZinc model
        self.model = mnz.Model()
        self.model.add_file("ProjSauteMouton.mzn")

        # Transform Model into a instance
        gecode = mnz.Solver.lookup("gecode")
        self.inst = mnz.Instance(gecode, self.model)


        self.nb_moutons = nombre_moutons
        self.inst["nbr_m"] = nombre_moutons

        self.moutons = []

        '''
        self.inst["nbr_sceau"] = len(liste_gallons)
        self.inst["remplissage_final"] = quantite_objectif

        list_taille_sceau = []
        list_remplissage_init = []
        for g in self.gallons:
            list_taille_sceau.append(g.taille)
            list_remplissage_init.append(g.remplissage)

        self.inst["taille_sceau"] = list_taille_sceau
        self.inst["remplissage_initial"] = list_remplissage_init
        '''


    def __str__(self):
        return "bla" #str(self.moutons)

    def __repr__(self):
        return self.__str__()

    def solve(self):
        # Solve the instance
        result = self.inst.solve(all_solutions=False)
        if len(result)==0:
            print("PAS DE SOLUTION")
            return False
        else:

            for i in range(len(result)):
                print(result["etat"])
                print(result["unsolved_step"])

            index = 0
            while result["unsolved_step"][index]==1:
                index+=1


            swap_sol=0
            #for sols in result["etat"]:
            final_list = []
            for i in range(len(result["unsolved_step"])):
                final_list.append(result["etat"][i*(self.nb_moutons*2+1):(i+1)*(self.nb_moutons*2+1)])
            #good_sub_list = result["etat"][index*(self.nb_moutons*2+1):(index+1)*(self.nb_moutons*2+1)]

            print(final_list)


            print("\nSOLUTION : ")
            #print(self.gallons)

            return True
