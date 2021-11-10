# -------------- Exercice48.py --------------
def remplacer(liste, enlever, mettre):
    liste = [x.replace(enlever, mettre) for x in liste]
    return liste





liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
print(remplacer(liste, liste[2], "Julien"))

