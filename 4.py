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
    def polcoef1(self):
        print("Entrez valeurs de coefs:\n")
        for degree in range(4,0,-1):
            coef = float(input(f"coefs x^{degree}:"))
            self.coefficients[4-degree] = coef
            
#########################################################

# addition pol

#pol = Polynome([2,0,1,3])
#print(pol)