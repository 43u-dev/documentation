mot = ["quoi","errath","fini"]


lettre =[]
motCache = []
for lettreDuMot in mot:
    lettre.append(lettreDuMot)
    motCache.append("-")


print(lettre)
print(motCache)




fin = False
essai  = 0
while essai < 9 and fin == False:
    reponse = input("Quelle est votre lettre ?")
    for lettreDeLaListe in lettre:
        if reponse == lettreDeLaListe:
            positionDeLaLettre = lettre.index(reponse)
            motCache[positionDeLaLettre] = lettreDeLaListe
    print(" ".join(motCache))
    etat = True
    for lettreCache in motCache:
        if lettreCache == "-":
            etat = False
    if etat == True:
        fin = True
    if etat == False:
        essai += 1
if fin == True:


    print("Bravo tu as gagné")
else:
    print("Tu as pris trop d'essai pour trouver ")

