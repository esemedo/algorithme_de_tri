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