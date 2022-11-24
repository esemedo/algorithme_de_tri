"""
Algorithme tri à bulle optimisé

tri-bulle-opti (tableau)
début
    longueur = longueur de tableau
    pour i allant jusqu'a longueur
        tableau_trie = vrai
        pour j allant de 0 à longueur-i-1
            si tableau[j+1] < tableau[j]
                inverser l'ordre de tableau[j+1] et tableau[j]
                tableau_trie = faux
            fin si
        fin pour
        si tableau_trie = vrai
            fin tri-bulle-opti
    fin pour
"""
def stat(min, max, step, nbr):
    pass
# créer un tableau de min element, un de max element, et un entre chaque step
# min = nb minimum d'element d'un tableau, max = nb max d'element d'un tableau, step = la step entre le nb d'elem de tableaux
# tableaux remplis aleatoirement
# nbr = nombre de tri d'un tableau a effectuer
# sortir le cout algo en moyenne pour chaque ensemble de tableaux d'x elements
# a faire pour les 4 algo, et donner le meilleur

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
            print(f"Coût algorithmique : {compteur_comparaison + compteur_affectation}")
            return

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