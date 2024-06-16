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

# multiplication de matrices OU scalaires
    def __mul__(self,oth):
        if isinstance(oth,Matrice): # is oth a Matrice?
            if self.cols != oth.lignes: # is Alines == B cols?
                raise ValueError("Matrices non multipliables, entrez les matrices telles que A(n,m) B(m,p)")
            resultat = [] # valeurs de C stockées ici
            for i in range(len(self.valeurs)):
                ligne = [] # valeurs de lignes 
                for j in range(len(oth.valeurs[0])):
                    sum = 0 # contiendra les elements a mettre dans ligne
                    for k in range(len(oth.valeurs)):
                        sum += self.valeurs[i][k] * oth.valeurs[k][j] # somme accumulée, self i*oth k et self k * oth j
                    ligne.append(sum)
                resultat.append(ligne)
            return Matrice(resultat)
        
        else: # oth != Matrice, scalaire
            resultat = [[element * oth for element in ligne] for ligne in self.valeurs] # multiplie chaque element de self par le scalaire
            return Matrice(resultat)
        
# transposition
    def transpose(self):
        resultat = [[self.valeurs[j][i] for j in range(self.lignes)] for i in range(self.cols)]
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



"""
# dummy matrixes to test
A = Matrice([[1,2],[3,4]])
B = Matrice([[1,2],[3,4]]) 
"""

# output 
def main():

# input de matrice par utilisateur
    print("Inserez matrice A:")
    A = creation()
    print("Matrice A:")
    print(A)

    print("Inserez matrice B:")
    B = creation()
    print("Matrice B:")
    print(B)
    
# operation a effectuer
    choix = input('operation a effectuer:\n Multiplication(M), Addition(A), Transpose(T)').upper()
    if choix == "M":
        multiplication = (A*B)
        print(multiplication)
        
    elif choix == "A":
       addition = (A+B)
       print(addition)
       
    elif choix == "T":
        print(f'la transpose de A est:\n{A.transpose()}\n la transpose de B est:\n{B.transpose()}')
        
if __name__ == "__main__":
    main()