# -------------- Exercice15.py --------------
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
i = 0
for lettre in str(phrase): 
    if lettre == lettre_a_chercher:
        i += 1 
print(str(i))

print(phrase.lower().count(lettre_a_chercher))