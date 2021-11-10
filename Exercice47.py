# -------------- Exercice47.py --------------
def additionner(nombre):
    return sum(map(int,str(nombre)))

nombre = 209812
print(additionner(nombre))



# ---------- Correction ---------
nombre = 209812
somme = sum([int(i) for i in str(nombre)])
print(somme)