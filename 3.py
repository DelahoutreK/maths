# considerons une fonction du second degré
# trois possibilitées, Delta pos, delta neg, delta = 0
# si delta > 0: x = -b+-sqrt(delta)/2
# si delta = 0: x = -b/2a
# si delta < 0: x = -b+-i sqrt(|delta|)/2a

# notons delta = b² - 4ac

equation = input("Entrer equation du second degre:\n").lower()

a = 0.0
b = 0.0
c = 0.0

termes = equation.split()

for terme in termes:
    if terme.endswith('x^2'):
        a_str = terme[:-3]
        a = float(a_str) if a_str else 1.0
    elif terme.endswith('x'):
        b_str = terme[:-1]
        b = float(b_str) if b_str else 1.0
    elif terme.isnumeric() or (terme[0]== '-' and terme[1:].isnumeric()):
        c = float(terme)
"""
for char in equation: 
    if char.isdigit(): # nb positifs
        if a == '':
            a += char
        elif b == '':
            b += char
        elif c == '':
            c += char
    elif char == '-' and (a == '' or b =='' or c == ''): # nb negatifs
        if b=='':
           b += char
        elif c == '':
            c += char
            
a = float(a) if a else 1.0
b = float(b) if b else 1.0
c = float(c) if c else 1.0
"""