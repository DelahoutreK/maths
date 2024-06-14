def encrypt(message, shift): # definition encryption
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ' # possibilités
    crypt = ''  # initialiser crypt

    for char in message: # boucle a travers les characteres du message et encrypte les possibilités
        if char in characters:
            ltr = (characters.index(char) + shift) % len(characters) # modulo pour permettre d'utiliser des shifts 0< ou >27
            crypt += characters[ltr]
    return crypt

def decrypt(crypt, shift): # def decryption
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    decryptmsg = ''

    for char in crypt:
        if char in characters:
            ltr = (characters.index(char) - shift) % len(characters) 
            decryptmsg += characters[ltr]
    return decryptmsg

question = input("Encrypt or decrypt?\n").lower() # selection encryption ou decryption
if question == "encrypt" or question == 'y':
    message = input("Message to encrypt:\n").upper() # user input pour le message a encrypter
    shift = int(input("inserez shift:\n")) # shift pour décaler les lettres du message
    crypt = encrypt(message, shift)
    print(f"Shift {shift}: {crypt}")

elif question == "decrypt" or question == "n":
    crypt = input("Message to decrypt:\n").upper()
    for shift in range(27): # boucle pour bruteforce toutes les possiblités, assumant qu'on ne connait pas le nombre de shifts
        decryptmsg = decrypt(crypt, shift)
        print(f"Shift {shift}: {decryptmsg}")

else:
    print("Entrer encrypt(y) ou decrypt(n), aucune autre valeur ne sera considérée.")
