def tri_selection(tab):
    nb_compa = 0
    nb_echange = 0
    for i in range(len(tab)): # On parcourt le tableau
        min = i # On considère que le minimum est le premier élément
        for j in range(i+1, len(tab)): # On parcourt le reste du tableau
            nb_compa += 1
            if tab[j] > tab[min]: # Si on trouve un élément plus grand
                min = j # On le considère comme nouveau minimum
        tab[i], tab[min] = tab[min], tab[i] # On échange les deux éléments
        nb_echange += 3

    return (nb_compa + nb_echange)

""""
tab = [1,10,291,2829,10,2903,20,9300,0,20]

best_case = sorted(tab)
worst_Case = sorted(tab, reverse = True)

print(tri_selection(tab))
print(tri_selection(best_case))
print(tri_selection(worst_case))

"""
