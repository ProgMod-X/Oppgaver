sparekonto = 10000
rente = 0.1
mål = 20000
vente = 0


while sparekonto < mål:
    sparekonto *= (1 + rente)
    vente += 1


print("Han må vente: ", vente, "år")