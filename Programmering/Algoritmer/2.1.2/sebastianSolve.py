import math 

sa, sb  = float(input("Hva er x-verdien til sentrumet av sirkelen ")), float(input("Hva er y-verdien til sentrumet av sirkelen "))
pa,pb = float(input("Hva er x-verdien til punktet du vil undersøke ")), float(input("Hva er y-verdien til punktet du vil undersøke "))
r = float(input("Hva er radiusen av sirkelen"))

distanse_fra_sentrum =  sqrt((sa - pa)**2 + (sb - pb)**2)

if distanse_fra_sentrum == r:
    print("på")
elif distanse_fra_sentrum > r:
    print("utenfor")
else:
    print("innenfor")