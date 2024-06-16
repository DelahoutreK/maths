class Matrice:
    def __init__(self,valeurs):
        self.valeurs = valeurs
        self.lignes = len(valeurs)
        self.cols = len(valeurs[0])
        
# format du rendu visuel de la matrice
    def __repr__(self): # renvoie une string
        return '\n'.join(['\t'.join(map(str,row))for row in self.valeurs])
    # \n retour a la ligne pour chaque ligne de la matrice
    # \t est juste une tabulation, map transforme les int en str pour etre sur
    
# addition de matrices
    def __add__(self,qt):
        if self.lignes != qt.lignes or self.cols != qt.cols:
            raise ValueError("erreur, matrices de dimensions différentes")
        resultat = []
        for i in range(self.lignes):
            ligne = [self.valeurs[i][j] + qt.valeurs[i][j] for j in range(self.cols)]
            resultat.append(ligne)
        return Matrice(resultat)

# fonction pour instancier les matrices via input
def creation():
    lignes = int(input("nb de lignes:"))
    cols = int(input("nb colonnes:"))
    valeurs = []
    for i in range(lignes):
        ligne = []
        for j in range(cols):
            valeur = int(input(f"valeurs pour ({i+1},{j+1})"))
            ligne.append(valeur)
        valeurs.append(ligne)
    return Matrice(valeurs)

# input de matrice par utilisateur
"""
print("Inserez matrice A:")
A = creation()
print("Matrice A:")
print(A)

print("Inserez matrice B:")
B = creation()
print("Matrice B:")
print(B)
"""
# dummy matrixes to test
A = Matrice([[1,2],[3,4]])
B = Matrice([[1,2],[3,4]]) 

# output 
try: 
    C = A + B
    print ("A+B=\n")
    for row in C.valeurs:
        print(row)

except ValueError as e:
    print(e)