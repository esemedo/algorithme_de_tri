def tri_insertion(T):
    comparaisons = 0
    affectations = 0
    for taille in range(1, len(T)):
        comparaisons += 1
        x = T[taille]

        A = taille - 1
        while A >= 0 and x < T[A]:
            affectations += 3
            T[A + 1] = T[A]
            A -= 1
        T[A + 1] = x
    return (comparaisons, affectations, T)

tab = [2, 7, 9, 90, 67, 45, 78, 24, 45, 89, 48, 3, 8, 99]

print("Cas aléatoire")
tri = tri_insertion(tab)
print("nombre de comparaisons :", tri[0])
print("nombre d'affectations :", tri[1])
print("résultat :", tri[2])
print("_____________________________________")


pire_cas = sorted(tab, reverse=True)

print("Pire Cas")
tri = tri_insertion(pire_cas)
print("nombre de comparaisons :", tri[0])
print("nombre d'affectations :", tri[1])
print("résultat :", tri[2])
print("_____________________________________")

meilleur_cas = sorted(tab)

print("Meilleur Cas")
tri = tri_insertion(meilleur_cas)
print("nombre de comparaisons :", tri[0])
print("nombre d'affectations :", tri[1])
print("résultat :", tri[2])
print("_____________________________________")