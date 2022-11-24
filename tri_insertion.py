#Fonction tri_insertion(T)

 #      pour taille de 1 à taille de T - 1
  #          x égal T[taille]

   #         A égal taille

     #       tant que j est plus grand que 0 et T[A - 1] plus grand que x
    #                 T[A] égal T[A - 1]
      #               A égal A- 1

       #     T[A] égal x
import random
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