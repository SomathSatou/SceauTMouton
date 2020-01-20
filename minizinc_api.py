# coding=utf-8
import minizinc
import class_gallons


g1 = class_gallons.Gallon(1,3)
g2 = class_gallons.Gallon(2,5)


list_gallon = []
list_gallon.append(g1)
list_gallon.append(g2)

model = class_gallons.Modelisation_Gallon(6,3,list_gallon)
model.solve()

print(model)


