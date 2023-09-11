def borderSum(liste):
    
    rad = len(liste)
    kolonne = len(liste[0])
    
    sum = 0

    # for i in range(1, rad - 1):
    #     sum += liste[i][0] + liste[i][kolonne - 1]

    for i in range(kolonne):
        sum += (liste[0][i] + liste[rad - 1][i])
    
    for i in range(1, rad - 1):
        sum += (liste[i][0] + liste[i][kolonne - 1])

    return sum

liste = [
    [1, 1, 0, 2],
    [3, 9, 8, 1],
    [1, 1, 1, 1]
]

resultat = borderSum(liste)
print("resultat av kode: ",resultat)  

# fiks denne rohaan!!!