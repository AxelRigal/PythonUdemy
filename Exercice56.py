# -------------- Exercice56.py --------------

texte = "Bonjour Udemy"

print("--------------")
for letter in range(len(texte)):
    phrase = ["|"] + [" " for j in range(2)] + [texte[letter]] + [" " for k in range(2)] + ["|"]
    print(*phrase)
print("--------------")