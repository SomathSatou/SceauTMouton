import minizinc
import class_gallons

# Create a MiniZinc model
model = minizinc.Model()
model.add_string("""
var -100..100: x;
int: a; int: b; int: c;
constraint a*(x*x) + b*x = c;
solve satisfy;
""")


# Transform Model into a instance
gecode = minizinc.Solver.lookup("gecode")
inst = minizinc.Instance(gecode, model)
inst["a"] = 1
inst["b"] = 4
inst["c"] = 0

# Solve the instance
result = inst.solve(all_solutions=True)
for i in range(len(result)):
    print("x = {}".format(result[i, "x"]))

g1 = class_gallons.Gallon(1,3)
g2 = class_gallons.Gallon(2,5)


list_gallon = []



list_gallon.append(g1)
list_gallon.append(g2)


model = class_gallons.Modelisation_Gallon(6,3,list_gallon)
print(model)
model.transfert(g1, g2)
print(model)
model.transfert(g1, g2)
print(model)
model.transfert(g2, g1)

print(model)


