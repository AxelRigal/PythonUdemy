# Exercice 7 ---- 
prenom = "Pierre"

# INSÉRER VOTRE CONDITION ICI.
# Votre condition doit vérifier si la variable prenom est bien une chaîne de caractère. Ici c'est le cas,
# votre condition doit donc être vraie et printer la phrase "La variable est une chaîne de caractères".

if type(prenom) is str:
    print("La variable est une chaîne de caractères")
if  type(prenom) != str:
    print()

# INSÉRER VOTRE CONDITION DE NOUVEAU
# Cette fois-ci, la variable n'est pas égale à une chaîne de caractère. Votre condition doit donc être fausse et 
# la phrase ne doit pas s'afficher.


# Correction 


prenom = "Pierre"
 
if type(prenom) == str:
    print("La variable est une chaîne de caractères")
 
prenom = 0
 
if isinstance(prenom, str):
    print("La variable est une chaîne de caractères")