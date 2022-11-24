"""
Algorithme de tri à bulles normal
Début
    Pour i parcourant tous le tableau:
        Pour j  allant de 0 à la longueur du tableau - i - 1:
            si tableau [j] est supérieur à tableau [j + 1] :
                valeur = tableau[j]
                tableau[j] = tableau[j + 1]
                tableau[j + 1] = valeur
            fin si
        fin pour
    fin pour
    Retourner le tableau trié
Fin

"""
import random
def tri_bulles(tab):
    cpt_comp = 0
    cpt_aff = 0
    for i in range(len(tab)-1): #pour pas calculer les derniers élements du tableau qui ont déjà été triée lors du parcours
        for j in range(len(tab)-i-1):
            cpt_comp += 1
            if tab[j] > tab[j+1]:
                (tab[j], tab[j+1]) = (tab[j+1], tab[j])
                cpt_aff += 3
    print("compteur de comparaison", cpt_comp, '/ compteur d\'affectations', cpt_aff)
    return tab

tab = [random.randint(1,100) for _ in range(11)]
print('tableau aléatoire\n',tab)
print('tri ordinaire -->',tri_bulles(tab))

#Résultat
tab3 = [random.randint(1,100) for _ in range(10)]
tab3.sort()
tab_trie = tab3
print('\n --- meilleur cas --- \n',tab_trie)
print('meilleure cas trie -->',tri_bulles(tab_trie))

tab2 = tab = [random.randint(1,100) for _ in range(10)]
tab2.sort(reverse = True)
tab_pire = tab2
print('\n ---- pire cas ---- \n', tab_pire)
print('pire cas trié -->',tri_bulles(tab_pire))

