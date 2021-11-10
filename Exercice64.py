# -------------- Exercice64.py --------------

import os
 
cur_dir = os.path.realpath(os.path.dirname(__file__))
print(cur_dir)
fichier = os.path.join(cur_dir, "fichier.txt")
 
with open(fichier, "w") as f:
    f.write("Bonjour tout le monde !")