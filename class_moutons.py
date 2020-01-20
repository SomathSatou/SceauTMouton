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
    def __init__(self, liste_moutons):

        # Create a MiniZinc model
        self.model = mnz.Model()
        #self.model.add_file("moutons.mzn")

        # Transform Model into a instance
        gecode = mnz.Solver.lookup("gecode")
        self.inst = mnz.Instance(gecode, self.model)

        self.moutons = liste_moutons



    def __str__(self):
        return str(self.moutons)

    def __repr__(self):
        return self.__str__()

    def solve(self):
        # Solve the instance
        result = self.inst.solve(all_solutions=False)
        if len(result)==0:
            print("PAS DE SOLUTION")
            return False
        else:
            '''
            #for i in range(len(result)):
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
            '''
            return True
