# -------------- Exercice45.py --------------
nombres = range(50)
nombres_pairs = []
for i in nombres:
    if i%2 == 0:
        nombres_pairs.append(i)
print(list(nombres_pairs))