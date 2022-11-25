tri_bulle_opti_result_file = "tri_bulle_opti_result.txt"

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

with open(tri_bulle_opti_result_file, 'w') as f:
    f.write("")
test = [4, 35, 77, 124, 4235, 43, 7, 54, 97, 42, 1, 65]

worst_case = sorted(test, reverse=True)
best_case = sorted(test)

with open(tri_bulle_opti_result_file, 'a') as f:
    f.write("Test de l'algo\n")
    f.write(f"{test}\n")
    f.write(f"Cout algorithmique : {tri_a_bulle_opti(test)}\n")
    f.write(f"{test}\n")
    f.write('--------------\n')
    f.write('Meilleur des cas\n')
    f.write(f"{best_case}\n")
    f.write(f"Cout algorithmique : {tri_a_bulle_opti(best_case)}\n")
    f.write(f"{best_case}\n")
    f.write('--------------\n')
    f.write('Pire des cas\n')
    f.write(f"{worst_case}\n")
    f.write(f"Cout algorithmique : {tri_a_bulle_opti(worst_case)}\n")
    f.write(f"{worst_case}\n")