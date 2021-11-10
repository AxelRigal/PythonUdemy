# -------------- Exercice27.py --------------
import os

fichier_courant = __file__
print(fichier_courant)

dossier_parent = os.path.dirname(fichier_courant)
print(dossier_parent)
#dossier_images =  os.path.join[dossier_parent, "images"]