# -------------- Exercice30.py --------------
from time import time
a = time()
_ = [i*2 for i in range(9999999)]
print(f"Temps d'exécution: {time() -a}s")
