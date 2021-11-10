# -------------- Exercice59.py --------------


def somme(a, b):
    if b < a:
        return sum(i for i in range(b, a+1))
    else:
        return sum(i for i in range(a, b+1))

print(somme(6,2))
print(somme(2,6))




# -------------- Correction -----------------
def somme(a, b):
    return sum(range(min(a, b), max(a, b) + 1))
 
print(somme(2, 6))
