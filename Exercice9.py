chaine = "Pierre, Julien, Anne, Marie, Lucien"
tabChaine = chaine.split(",")
tabChaine = [x.strip(' ') for x in tabChaine]
tabChaine.sort()
separator = (', ')
chaine = separator.join(tabChaine)
print(chaine)


# ------- Correction -----

chaine = "Pierre, Julien, Anne, Marie, Lucien"
 
chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_en_ordre)