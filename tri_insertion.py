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
"""
tab = []
i = 1
for i in range(1, 31):
    i += 1

    tab.append(random.randrange(1, 1000))

print("Cas aléatoire")
tri = tri_insertion(tab)
print("nombre de comparaisons :", tri[0])
print("nombre d'affectations :", tri[1])
print("résultat :", tri[2])
print("_______________________________________________________________")


pire_cas = sorted(tab, reverse=True)

print("Pire Cas")
tri = tri_insertion(pire_cas)
print("nombre de comparaisons :", tri[0])
print("nombre d'affectations :", tri[1])
print("résultat :", tri[2])
print("______________________________________________________________")

meilleur_cas = sorted(tab)

print("Meilleur Cas")
tri = tri_insertion(meilleur_cas)
print("nombre de comparaisons :", tri[0])
print("nombre d'affectations :", tri[1])
print("résultat :", tri[2])
print("______________________________________________________________")

print(random.randrange(1, 1000))
"""