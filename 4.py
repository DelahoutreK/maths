# definition d'un polynome 
class Polynome: # classe python pour stocker mes polynomes
    def __init__(self, coefficients=None):
        if coefficients is None:
            self.coefficients = [0] * 4
        else:
            self.coefficients = coefficients
    
    def __str__(self): # stringify
        termes = []
        for degree in range (4,0,-1):
            coef = self.coefficients[4- degree]
            if coef !=0:
                termes.append(f'{coef}x^{degree}')
        return " + ".join(termes) if termes else "0"


#########################################################

# input de polynome 
    def polcoef(self):
        print("Entrez valeurs de coefs:\n")
        for degree in range(4,0,-1):
            coef = float(input(f"coefs x^{degree}:"))
            self.coefficients[4-degree] = coef
            
#########################################################

# addition pol
    def add(self,oth):
        resultat = [self.coefficients[i] + oth.coefficients[i] for i in range(4)]
        return Polynome(resultat)

#########################################################

# multiplication par reel
    def multR(self,scal):
        resultat = [coef*scal for coef in self.coefficients]
        return Polynome(resultat)

#########################################################

def main(): # definition de la fct calculatrice
    print("Premier Polynome:\n")
    p1=Polynome()
    p1.polcoef()
    print(p1)
    
    # addition de polynome (call de la methode)
    choix = input("Addition de polynomes?(A)\nMulitiplication par reel?(R)\nMultiplication par polynome?(M)\n")
    if choix == "A" or choix == "a":
        print("Second Polynome:\n")
        p2=Polynome()
        p2.polcoef()
        print(p2)
        sum = p1.add(p2)
        print(sum)
    
    # multiplication par reel
    elif choix == "R" or choix == 'r':
        print("Inserez valeur a multiplier:\n")
        reel = input("valeur a multiplier:\n")
        rprod = p1.multR(reel)
        print(rprod)
        
if __name__ == "__main__": # call de main() si elle existe
    main()
#pol = Polynome([2,0,1,3])
#print(pol)