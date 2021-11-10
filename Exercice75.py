# -------------- Exercice75.py --------------

phrase = "Phrase en camel case"
phrase = phrase.lower()
phrase_tab = phrase.split()
phrase_out = ""
for x in phrase_tab:
    if x == phrase_tab[0]:
        phrase_out += x
    else :
        phrase_out += x.capitalize()

print(phrase_out)


