# considerons une fonction du second degré
# trois possibilitées, Delta pos, delta neg, delta = 0
# si delta > 0: x = -b+-sqrt(delta)/2
# si delta = 0: x = -b/2a
# si delta < 0: x = -b+-i sqrt(|delta|)/2a

# notons delta = b² - 4ac

equation = input("Entrer equation du second degre:\n")

a = ""
b = ""
c = ""

for char in equation: 
    if char.isdigit():
        if a == '':
            a += char
        elif b == '':
            b += char
        elif c == '':
            c += char
    elif char == '-' and (a == '' or b =='' or c == ''):
        if b=='':
           b += char
        elif c == '':
            c += char