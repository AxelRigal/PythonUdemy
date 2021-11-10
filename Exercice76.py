# -------------- Exercice76.py --------------
import string
phrase = "Bonjour tout le monde"
phrase_tab = phrase.split()
resultat = []
for x in reversed(phrase_tab):
    resultat.append(x)

resultat_formate = " ".join(resultat).capitalize()
print(resultat_formate)
