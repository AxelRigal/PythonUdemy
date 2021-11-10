# -------------- Exercice33.py --------------
mot = "Udemy"
for x in reversed(mot):
    print(x)
print("".join(reversed(mot)).lower().capitalize())
print(mot[::-1].capitalize())