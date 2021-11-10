# -------------- Exercice78.py --------------
def middle(s):
    if len(s) == 0:
        return ""
    elif len(s) % 2 != 0:
        return s[len(s)//2]
    elif len(s) % 2 == 0:
        return s[len(s)//2 - 1] + s[len(s)//2]

mot = "Un roc cornu"
mot_join = mot.replace(" ", "")
mot_join.lower()
for x in reversed(len(mot_join/2)) :
    for y in len(mot_join/2) :
        if x != y:
            print(False)
        print(True)
    
print(mot_join)