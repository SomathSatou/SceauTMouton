# coding=utf-8
import minizinc
import class_moutons as m




model = m.Modelisation_Mouton( liste_moutons=[ m.Mouton(numero=1, couleur=1), m.Mouton(numero=2, couleur=1), m.Mouton(numero=3, couleur=1),
                                                           m.Mouton(numero=4, couleur=2), m.Mouton(numero=5, couleur=2), m.Mouton(numero=6, couleur=2)
                                                           ])

print(model)
model.solve()





