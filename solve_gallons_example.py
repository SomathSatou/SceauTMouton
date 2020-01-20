# coding=utf-8
import minizinc
import class_gallons


g1 = class_gallons.Gallon(numero=1,taille=10, remplissage_inital=10)
g2 = class_gallons.Gallon(numero=2,taille=7,remplissage_inital=0)
g3 = class_gallons.Gallon(numero=3,taille=2,remplissage_inital=0)


list_gallon = []
list_gallon.append(g1)
list_gallon.append(g2)
list_gallon.append(g3)

model = class_gallons.Modelisation_Gallon(quantite_objectif=4, liste_gallons=list_gallon)
model.solve()





