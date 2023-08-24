sparekonto = 10000
rente = 0.1
år = 5
mål = 20000
vente = 0

# A
sum = sparekonto * (1 + rente)**år
print("A:\nEtter 5 år har han:", round(sum,3), "kr på konto\n")

# B
while sparekonto < mål:
    sparekonto *= (1 + rente)
    vente += 1


print("B:\nHan må vente: ", vente, "år")