
""""
Algorithme de tri par sélection

procédure tri_selection(tableau t)
      n ← longueur(t) 
      pour i de 0 à n - 2
          min ← i       
          pour j de i + 1 à n - 1
              si t[j] < t[min], alors min ← j
          fin pour
      fin pour
  fin procédure
"""


tab = [1,10,291,2829,10,2903,20,9300,0,20]
def tri_selection(tab):
    for i in range(len(tab)): # On parcourt le tableau
        min = i # On considère que le minimum est le premier élément
        for j in range(i+1, len(tab)): # On parcourt le reste du tableau
            if tab[j] < tab[min]: # Si on trouve un élément plus petit
                min = j # On le considère comme nouveau minimum
        tab[i], tab[min] = tab[min], tab[i] # On échange les deux éléments
    return tab # On retourne le tableau trié
   
print(tri_selection(tab))