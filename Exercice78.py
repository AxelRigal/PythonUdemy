# -------------- Exercice78.py --------------
mot = "Un roc cornu"
mot_join = mot.replace(" ", "")
mot_join = mot_join.lower()
taille_divise = len(mot_join)//2 
palindrome = False
for x in range(taille_divise):
    for y in range(len(mot_join)-1, taille_divise, -1):
        if mot_join[x] == mot_join[y]: 
            mot_join = mot_join[:-1]
            break
        print(False)

print(True)




# --------- Correction 
 
mot = "Un roc cornu"
 
mot_lower = mot.lower().replace(" ", "")
 
if mot_lower == mot_lower[::-1]:
    print(True)
else:
    print(False) 