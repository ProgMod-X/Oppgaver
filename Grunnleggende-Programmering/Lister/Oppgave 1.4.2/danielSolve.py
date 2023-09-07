import random

antall = 100
liste = []

for i in range(antall): 
    liste.append(random.randint(1,antall))
    
gjennomsnitt = sum(liste)/antall
min = min(liste)
max = max(liste)

print("Gjennomsnitt: ", gjennomsnitt, "Min: ", min, "Max: ", max)