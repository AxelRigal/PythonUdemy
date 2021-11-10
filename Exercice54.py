# -------------- Exercice54.py --------------
symbole = "*"
compte = 0
for i in range(14):
    if i < 7:
        compte += 1
        print(symbole * compte)
    elif i >=7:
        compte -= 1
        print(symbole * compte)