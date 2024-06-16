class Matrice:
    def __init__(self,valeurs):
        self.valeurs = valeurs
        self.lignes = len(valeurs)
        self.cols = len(valeurs[0])
        
    def __repr__(self): # renvoie une string
        return '\n'.join(['\t'.join(map(str,row))for row in self.valeurs])
    # \n retour a la ligne pour chaque ligne de la matrice
    # \t est juste une tabulation, map transforme les int en str pour etre sur
    
    def __add__(self,qt):
        if self.lignes != qt.lignes or self.cols != qt.cols:
            raise ValueError("erreur, matrices de dimensions différentes")
        resultat = []
        for i in range(self.lignes):
            ligne = [self.valeurs[i][j] + qt.valeurs[i][j] for j in range(self.cols)]
            resultat.append(ligne)
        return Matrice(resultat)
   
A = Matrice([[1,2],[3,4]])
B = Matrice([[1,2],[3,4]]) 

try: 
    C = A + B
    print ("A+B=\n")
    for row in C.valeurs:
        print(row)

except ValueError as e:
    print(e)