import random
tri_insertion_result_file = "tri_insertion_result.txt"
def tri_insertion(T):
    comparaisons = 0
    affectations = 0
    for taille in range(1, len(T)):
        x = T[taille]
        A = taille - 1
        comparaisons += 1
        while A >= 0 and x < T[A]:
            affectations += 3
            T[A + 1] = T[A]
            A -= 1
        T[A + 1] = x
    return (comparaisons + affectations)

with open(tri_insertion_result_file, 'w') as f:
    f.write("")
tab = []
i = 1
for i in range(1, 10):
    i += 1

    tab.append(random.randrange(1, 1000))
tri = tab
pire_cas = sorted(tab, reverse=True)
meilleur_cas = sorted(tab)


with open(tri_insertion_result_file, 'a') as f:
    f.write("Cas aléatoire\n")
    f.write(f"{tri}\n")
    f.write(f"Cout algoritmique : {tri_insertion(tri)}\n")
    f.write(f"{tri}\n")
    f.write("_______________________________________________________________\n")
    f.write("Pire Cas\n")
    f.write(f"{pire_cas}\n")
    f.write(f"Cout algoritmique : {tri_insertion(pire_cas)}\n")
    f.write(f"{pire_cas}\n")
    f.write("______________________________________________________________\n")
    f.write("Meilleur Cas\n")
    f.write(f"{meilleur_cas}\n")
    f.write(f"Cout algoritmique : {tri_insertion(meilleur_cas)}\n")
    f.write(f"{meilleur_cas}\n")