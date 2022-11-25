tri_selection_result_file = "tri_selection_result.txt"

def tri_selection(tab):
    nb_compa = 0
    nb_echange = 0
    for i in range(len(tab)): # On parcourt le tableau
        min = i # On considère que le minimum est le premier élément
        for j in range(i+1, len(tab)): # On parcourt le reste du tableau
            nb_compa += 1
            if tab[j] < tab[min]: # Si on trouve un élément plus grand
                min = j # On le considère comme nouveau minimum
        tab[i], tab[min] = tab[min], tab[i] # On échange les deux éléments
        nb_echange += 3
    return (nb_compa + nb_echange)

with open(tri_selection_result_file, 'w') as f:
    f.write("")
tab = [1,10,291,2829,10,2903,20,9300,0,20, 11]

best_case = sorted(tab)
worst_case = sorted(tab, reverse=True)
with open(tri_selection_result_file, 'a') as f:
    f.write('--------------\n')
    f.write('Test Algo\n')
    f.write(f"{tab}")
    f.write(f"Cout algoritmique : {tri_selection(tab)}\n")
    f.write(f"{tab}\n")
    f.write('--------------\n')
    f.write('Meilleur des cas\n')
    f.write(f"{best_case}\n")
    f.write(f"Cout algoritmique : {tri_selection(best_case)}\n")
    f.write(f"{best_case}\n")
    f.write('--------------\n')
    f.write('Pire des cas\n')
    f.write(f"{worst_case}\n")
    f.write(f"Cout algoritmique : {tri_selection(worst_case)}\n")
    f.write(f"{worst_case}\n")