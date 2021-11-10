# -------------- Exercice34.py --------------
import random

mot = "Bonjour"
mot = list(mot)
random.shuffle(mot)

mot_random = "".join(mot).capitalize()

print(mot_random)