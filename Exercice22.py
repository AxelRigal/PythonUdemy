# -------------- Exercice22.py --------------

employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes.get("01", {}).get("identite", {}).get("prenom"))
print(employes.get("01").get("identite").get("prenom"))


# ------ Correction ----------

employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))
