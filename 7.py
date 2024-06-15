# systeme d'equation a trois inconnues
class Equation:
    def __init__(self, x, y, z, c):
        self.x = x
        self.y = y
        self.z = z
        self.c = c
        
# determinant d'une matrice
def determinant(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    return x1 * (y2 * z3 - z2 * y3) - y1 * (x2 * z3 - z2 * x3) + z1 * (x2 * y3 - y2 * x3)

# definition solution
def soluce(eq1, eq2,eq3):
    x1, y1, z1, c1 = eq1.x, eq1.y, eq1.z, eq1.c
    x2, y2, z2, c2 = eq2.x, eq2.y, eq2.z, eq2.c
    x3, y3, z3, c3 = eq3.x, eq3.y, eq3.z, eq3.c    
    
# mise en variable du determinant
    det = determinant(x1, y1, z1, x2, y2, z2, x3, y3, z3)

    if det == 0:
        raise ValueError("pas de solution unique")

# calcul de sous determinant (cramer)
    deta = determinant(c1,y1,z1,c2,y2,z2,c3,y3,z3)
    detb = determinant(x1,c1,z1,x2,c2,z2,x3,c3,z3)
    detc = determinant(x1,y1,c1,x2,y2,c2,x3,y3,c3)
    
    a = deta/det
    b = detb/det
    c = detc/det
    
    return a,b,c

# input equation 1
x1 = float(input("coefficient equation 1, x:\n"))
y1 = float(input("coefficient equation 1, y:\n"))
z1 = float(input("coefficient equation 1, z:\n"))
c1 = float(input("coefficient equation 1, c:\n"))

# input equation 2
x2 = float(input("coefficient equation 2, x:\n"))
y2 = float(input("coefficient equation 2, y:\n"))
z2 = float(input("coefficient equation 2, z:\n"))
c2 = float(input("coefficient equation 2, c:\n"))

# input equation 3
x3 = float(input("coefficient equation 3, x:\n"))
y3 = float(input("coefficient equation 3, y:\n"))
z3 = float(input("coefficient equation 3, z:\n"))
c3 = float(input("coefficient equation 3, c:\n"))

# instanciations 
eq1 = Equation(x1,y1,z1,c1)
eq2 = Equation(x2,y2,z2,c2)
eq3 = Equation(x3,y3,z3,c3)

# output
try:
    a,b, c = soluce(eq1,eq2,eq3)
    print(f"solution: x = {a:.3f}, y={b:.3f}, z={c:.3f}")
except ValueError as e:
    print(e)