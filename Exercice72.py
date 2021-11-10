# -------------- Exercice72.py --------------

from datetime import date 

date_ancienne = date.fromisoformat('2014-07-02')
date_recente =  date.fromisoformat('2018-07-11')
nb_jours = (date_recente - date_ancienne).days

print(nb_jours)