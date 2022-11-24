
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

print("------------------------------------------------")

"""
Ajoutez un compteur des comparaisons et un des échanges/affectations dans le tableau (un
échange vaut 3 affectations) :
"""



def tri_selection2(tab):
    nb_compa = 0
    nb_echange = 0
    for i in range(len(tab)): # On parcourt le tableau
        nb_compa += 1
        min = i # On considère que le minimum est le premier élément
        for j in range(i+1, len(tab)): # On parcourt le reste du tableau
            nb_compa += 1
            if tab[j] < tab[min]: # Si on trouve un élément plus petit
                min = j # On le considère comme nouveau minimum
        tab[i], tab[min] = tab[min], tab[i] # On échange les deux éléments
        nb_echange += 3
    print("Le nombre de comparaison est de : ", nb_compa, "et le nombre d'échange est de : ", nb_echange)
    return tab

    

print(tri_selection2(tab))

print("------------------------------------------------")

"""Jeux d'essais avec le meilleur et le pire cas"""


def tri_selection3(tab):
    nb_compa = 0
    nb_echange = 0
    for i in range(len(tab)): # On parcourt le tableau
        nb_compa += 1
        min = i # On considère que le minimum est le premier élément
        for j in range(i+1, len(tab)): # On parcourt le reste du tableau
            nb_compa += 1
            if tab[j] > tab[min]: # Si on trouve un élément plus grand
                min = j # On le considère comme nouveau minimum
        tab[i], tab[min] = tab[min], tab[i] # On échange les deux éléments
        nb_echange += 3
    print("Le nombre de comparaison et d'échanges est de : ", nb_compa, "et le nombre d'échange est de : ", nb_echange)
    print ("pire cas :",tab)
    for i in range(len(tab)): # On parcourt le tableau
        nb_compa += 1
        min = i # On considère que le minimum est le premier élément
        for j in range(i+1, len(tab)): # On parcourt le reste du tableau
            nb_compa += 1
            if tab[j] < tab[min]: # Si on trouve un élément plus grand
                min = j # On le considère comme nouveau minimum
        tab[i], tab[min] = tab[min], tab[i] # On échange les deux éléments
        nb_echange += 3
    print("Le nombre de comparaison et d'échanges est de : ", nb_compa, "et le nombre d'échange est de : ", nb_echange)
    print("le meilleur cas :",tab)
    print("Le nombre de comparaison et d'échanges est de : ", nb_compa, "et le nombre d'échange est de : ", nb_echange)
    return ""
    

print(tri_selection3(tab))




