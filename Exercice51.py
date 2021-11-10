# -------------- Exercice51.py --------------
employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
for l in liste:
    if type(l) is str:
        employes.update({"id-{:02d}".format(len(employes)+1) : l})
print(employes)