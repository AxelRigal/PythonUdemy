# -------------- Exercice52.py --------------
import string
alphabet = string.ascii_lowercase
tab  = {int(i+1) : alphabet[i] for i in range(len(alphabet))}
print(tab)