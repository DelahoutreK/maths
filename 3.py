# apres avoir recherché le sujet plus en profondeur, utiliser une liste pour stocker les valeurs de l'equation aurait été probablement plus simple

#import cmath
equation = input("Entrer equation du second degre (ax^2 + bx + c), la notation est importante!:\n").lower()

a = 0.0
b = 0.0
c = 0.0

termes = equation.split()

for terme in termes:
    if terme.endswith('x^2'): # selectionne A 
        a_str = terme[:-3]
        a = float(a_str) if a_str else 1.0
    elif terme.endswith('x'):   # selectionne B
        b_str = terme[:-1]
        b = float(b_str) if b_str else 1.0
    elif terme.isnumeric() or (terme[0] == '-' and terme[1:].isnumeric()): # selectione C et vérifie si positif ou negatif
        c = float(terme)
        
#delta = (b*b)-(4*a*c)
delta = 0
print(f"delta vaut {delta}")

if delta > 0: # gere un delta positif
    sol1 = round((-b+(delta**0.5))/(2*a),2)
    sol2 = round((-b-(delta**0.5))/(2*a),2)
    print(f"{sol1} et {sol2}")


elif delta == 0: # gere un delta nul
    sol1 = round(-b/(2*a),2)
    print(f"La solution est {sol1}")

elif delta < 0: # delta negatif
    print("delta est un complexe.") 
    #sol1 = (-b + cmath.sqrt(-delta))/(2*a)
    #sol2 = (-b - cmath.sqrt(-delta))/(2*a)
    #print(f"solutions: {sol1} et {sol2}")
