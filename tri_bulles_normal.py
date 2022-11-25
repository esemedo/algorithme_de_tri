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
    return (cpt_aff + cpt_comp)

tab = [random.randint(1,100) for _ in range(11)]

pire = sorted(tab, reverse=True)
meilleur = sorted(tab)
#Résultat
with open ('tri_bulles_normal_result.txt','w') as f :
    f.write(f"--- tableau aléatoire ---\n {tab}\n")
    f.write(f"coût algorithmique : {tri_bulles(tab)}\n")
    f.write(f"tableau aléatoire trié --> {tab}\n")

    f.write(f"\n --- meilleur cas --- \n {meilleur}\n")
    f.write(f"coût algorithmique : {tri_bulles(meilleur)}\n")
    f.write(f"meilleure cas trie --> {meilleur}\n")

    f.write(f"\n ---- pire cas ---- \n {pire}\n")
    f.write(f"coût algorithmique :  {tri_bulles(pire)}\n")
    f.write(f"pire cas trié -->' {pire}\n")
