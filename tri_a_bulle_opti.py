def tri_a_bulle_opti(tableau):
    length = len(tableau)
    compteur_comparaison = 0
    compteur_affectation = 0
    for i in range(length):
        tableau_trie = True
        for j in range(0, length-i-1):
            compteur_comparaison += 1
            if tableau[j+1] < tableau[j]:
                compteur_affectation += 3
                tableau[j+1], tableau[j] = tableau[j], tableau[j+1]
                tableau_trie = False
        if tableau_trie:
            cout_algo = compteur_comparaison + compteur_affectation
            return cout_algo
"""
test = [4, 35, 77, 124, 4235, 43, 7, 54, 97, 42, 1, 65]

worst_case = sorted(test, reverse=True)
best_case = sorted(test)

print("Test de l'algo")
print(test)
tri_a_bulle_opti(test)
print(test)
print('--------------')
print('Meilleur des cas')
print(best_case)
tri_a_bulle_opti(best_case)
print(best_case)
print('--------------')
print('Pire des cas')
print(worst_case)
tri_a_bulle_opti(worst_case)
print(worst_case)
"""