# -------------- Exercice60.py --------------
import string
employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]
employe_avant_m = []
employe_apres_m = []
for employe in employes:
    #print(employe[0])
    if employe[0] >= "M":
        employe_apres_m.append(employe)
    else:
        employe_avant_m.append(employe)

#print(employe_avant_m)
#print(employe_apres_m)

# ------------ Correction ------------------

employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]

alphabet = string.ascii_lowercase
milieu=int(len(alphabet)/2)
alphabet_01, alphabet_02 = alphabet[:milieu], alphabet[milieu:]
employe_avant_m = []
employe_apres_m = []

for employe in employes:
    if employe[0].lower() in alphabet_01:
        employe_avant_m.append(employe)
    elif employe[0].lower() in alphabet_02:
        employe_apres_m.append(employe)

print(employe_avant_m)
print(employe_apres_m)