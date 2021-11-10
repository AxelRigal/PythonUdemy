# -------------- Exercice29.py --------------

import os 
env_var = os.environ.get("Path")
tab  = env_var.split(";")
for x in tab: print(x)

