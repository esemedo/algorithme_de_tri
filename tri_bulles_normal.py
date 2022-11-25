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
                cpt_aff += 3
                (tab[j], tab[j+1]) = (tab[j+1], tab[j])
    #print("compteur de comparaison", cpt_comp, '/ compteur d\'affectations', cpt_aff, '\ncoût algorithmique :', cpt_aff + cpt_comp)
    return (cpt_aff + cpt_comp)
"""
tab = [random.randint(1,100) for _ in range(11)]
pire = sorted(tab, reverse=True)
meilleur = sorted(tab)

#Résultat
print('tableau aléatoire\n',tab)
print('tri ordinaire -->',tri_bulles(tab))

print('\n --- meilleur cas --- \n',meilleur)
print('meilleure cas trie -->',tri_bulles(meilleur))

print('\n ---- pire cas ---- \n', pire)
print('pire cas trié -->',tri_bulles(pire))
"""