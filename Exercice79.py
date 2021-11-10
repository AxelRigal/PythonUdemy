# -------------- Exercice79.py --------------
import string

phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
alphabet = string.ascii_lowercase
phrase = phrase.lower()
longueur_alphabet = len(alphabet)
for x in range(len(phrase)):
    for y in range(longueur_alphabet):
        if phrase[x] == alphabet[y]:
            alphabet = alphabet.replace(alphabet[y], "")
            longueur_alphabet = longueur_alphabet - 1
            break
if alphabet == "":
    print("La phrase est un Pangramme")

# --------- Correction -------

import string
 
phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
phrase_lower = phrase.lower()
 
alphabet = list(string.ascii_lowercase)
 
for l in phrase_lower:
    if l in alphabet:
        alphabet.remove(l)
 
if alphabet:
    print("La phrase n'est pas un Pangramme")
else:
    print("La phrase est un Pangramme")
