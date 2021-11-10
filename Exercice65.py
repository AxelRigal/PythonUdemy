# -------------- Exercice65.py --------------

def diviseur(nombre):
    diviseurs = []
    for i in range(1, nombre+1):
        if nombre%i == 0 :
            diviseurs.append(i)
    return diviseurs

nombre = 50

print(diviseur(nombre))
