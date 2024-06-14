def polynome():
    print("entrer coefficients de degrés quatre a un")
    coefficients =[]
    
    for degree in range (4,0,-1):
        coef = float(input(f'coefs: x^{degree}'))
        coefficients.append(coef)