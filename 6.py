# systeme d'equation a deux inconnues
class Equation:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
# methode de résolution
def soluce(eq1, eq2):
    x1, y1, z1 = eq1.x, eq1.y, eq1.z
    x2, y2, z2 = eq2.x, eq2.y, eq2.z
    
#calcul du determinant
    determinant = x1*y2-x2*y1
    
    if determinant == 0:
        raise ValueError("pas de solution unique")
    
    a = (z1 * y2 - z2 * y1)/determinant
    b = (x1 * z2 - x2 * z1)/determinant
    
    return a,b

# user input equation 1
x1 = float(input("coefficient equation 1, x:\n"))
y1 = float(input("coefficient equation 1, y:\n"))
z1 = float(input("coefficient equation 1, c:\n"))

# user input equation 2
x2 = float(input("coefficient equation 2, x:\n"))
y2 = float(input("coefficient equation 2, y:\n"))
z2 = float(input("coefficient equation 2, c:\n"))

# instanciation objets
eq1 = Equation(x1,y1,z1)
eq2 = Equation(x2,y2,z2)

# output
try:
    a,b = soluce(eq1,eq2)
    print(f"solution: x = {a}, y={b}")
except ValueError as e:
    print(e)