'''
Vi setter 10000 kr inn på en sparekonto med 10% rente årlig rente.

A) Hvor mye penger er på kontoen etter 5 år?

B) Hvor mange år må vi vente før det er over 20000 kr på kontoen?
'''


startbeløp = 10000 
rente = 0.1
år = 5

#A) 

total_kapital= startbeløp * (1 + rente) ** år

print("Etter 5 år har vi", round(total_kapital),"kr")

#B)

år = 0
total_kapital = 10000
mål = 20000


while total_kapital < mål:
    total_kapital *= (1 + rente) ** 2
    år += 1 
print("Vi må vente", år, "år før vi får", mål,"kr")