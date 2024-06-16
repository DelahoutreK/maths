def keygen(p,q):
    n = p*q #
    phi = (p-1)*(q-1)
    

    while True:
        try:
            e = int(input("exposant a utiliser:\n"))        
            if e <= 1 or e >= phi or gcd(e, phi) != 1:
                print("exposant invalide")
                continue

            # exposant privé
            d = inv(e, phi)
        
            # keys
            return ((e,n),(d,n))
        
        except ValueError:
            print("Erreur, e doit etre un entier")
            
def gcd(a,b): # PGCD
    while b!= 0:
        a,b = b,a % b
    return a
    
def inv(a,m): # inversé modulaire de a modulo m (entier x tq axx = 1)
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1: # exception, si m = 1 l'inverse modulaire n'existe pas
        q = a // m # quotient de a par m
        m, a = a % m,m  # m = a modulo m et a = m
        x0, x1 = x1 - q * x0, x0 # euclide étendu, pcgd
    if x1 < 0:
        x1 += m0 # permet d'avoir un résultat positif
    return x1

def encrypt(msg, public_key):
    e, n = public_key # attribution de valeurs
    m = int.from_bytes(msg.encode(),"big") # conversion en int
    c = pow(m, e, n) # chiffrement
    return c

p = int(input("valeur de p:\n"))
q = int(input("valeur de q:\n"))

public_key, private_key = keygen(p,q)
print("clé pub:\n", public_key)
print("clé priv:\n",private_key)