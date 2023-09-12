#A)

import random as rd 
'''

x,y = rd.randint(1,10),rd.randint(1,10)

svar = int(input(f"Hva er {x} * {y}? "))

if svar == x*y:
    print("Riktig!")
else: 
    print("Feil")
'''

#B) 

'''
while True:
    x,y = rd.randint(1,10),rd.randint(1,10)
    
    svar = int(input(f"Hva er {x} * {y}? "))

    if svar == x*y:
        print("Riktig!")
    else:
        print("Feil") 
        break
'''

#C) 
'''
antall = int(input("Hvor mange runder vil du spille? "))
score = 0
for i in range(antall):
    x,y = rd.randint(1,10),rd.randint(1,10)
    
    svar = int(input(f"Hva er {x} * {y}? "))

    if svar == x*y:
        print("Riktig!")
        score += 1 
    else:
        print("Feil") 

if score == antall:
    print(f"Perfekt, du fikk {score} av {antall} mulig poeng. ")
elif score/antall>0.66:
    print(f"Bra!, du fikk {score} av {antall} mulig poeng. ")
elif 0.33<= score/antall<=0.66:
    print(f"Du trenger mer trening... , du fikk {score} av {antall} mulig poeng. ")
else:
    print(f"Spør mattelæreren din om hjelp!, du fikk {score} av {antall} mulig poeng. ")
'''
'''
dif = str(input("Først og fremst, hvor vanskelig vil du at det skal være? Enkel, middels eller vanskelig? "))
antall = int(input("Hvor mange runder vil du spille? "))
score = 0
if dif == "enkel":
    dif = 10
    print(f"Vanskeliggrad satt til enkel")
elif dif == "middels":
    dif = 25
    print(f"Vanskeliggrad satt til middels")
else:
    dif = 100
    print(f"Vanskeliggrad satt til vanskelig")
for i in range(antall):
    
    x,y = rd.randint(1,dif),rd.randint(1,dif)
    
    svar = int(input(f"Hva er {x} * {y}? "))

    if svar == x*y:
        print("Riktig!")
        score += 1 
    else:
        print("Feil") 

if score == antall:
    print(f"Perfekt, du fikk {score} av {antall} mulig poeng. ")
elif score/antall>0.66:
    print(f"Bra!, du fikk {score} av {antall} mulig poeng. ")
elif 0.33<= score/antall<=0.66:
    print(f"Du trenger mer trening... , du fikk {score} av {antall} mulig poeng. ")
else:
    print(f"Spør mattelæreren din om hjelp!, du fikk {score} av {antall} mulig poeng. ")
'''

#D)
#Utvid spillet til å også omfatte addisjon, subtraksjon og divisjon (mulig en blanding?).

'''
def velg_vanskelighetsgrad():
    vanskelighetsgrad = input("Først og fremst, hvor vanskelig vil du at det skal være? Enkel, middels eller vanskelig? ").lower()
    if vanskelighetsgrad == "enkel":
        return 10
    elif vanskelighetsgrad == "middels":
        return 25
    else:
        return 100

def spille_runde(dif):
    x, y = random.randint(1, dif), random.randint(1, dif)
    svar = int(input(f"Hva er {x} * {y}? "))
    if svar == x * y:
        print("Riktig!")
        return 1
    else:
        print("Feil")
        return 0

def main():
    dif = velg_vanskelighetsgrad()
    antall = int(input("Hvor mange runder vil du spille? "))
    antall_multiplikasjon = int(input("Hvor mange runder med multiplikasjon vil du spille? "))
    antall_addisjon = int(input("Hvor mange runder med addisjon vil du spille? "))
    antall_divisjon = int(input("Hvor mange runder med divisjon vil du spille? "))
    antall_subtraksjon = int(input("Hvor mange runder med subtraksjon vil du spille? "))
    score = 0

    for _ in range(antall_multiplikasjon):
        score += spille_runde(dif)

    for _ in range(antall_addisjon):
        score += spille_runde(dif)

    for _ in range(antall_divisjon):
        score += spille_runde(dif)

    for _ in range(antall_subtraksjon):
        score += spille_runde(dif)

    resultat_prosent = score / (antall_multiplikasjon + antall_addisjon + antall_divisjon + antall_subtraksjon) * 100

    if resultat_prosent == 100:
        print(f"Perfekt, du fikk {score} av {antall} mulig poeng.")
    elif resultat_prosent > 66:
        print(f"Bra!, du fikk {score} av {antall} mulig poeng.")
    elif resultat_prosent > 33:
        print(f"Du trenger mer trening..., du fikk {score} av {antall} mulig poeng.")
    else:
        print(f"Spør mattelæreren din om hjelp!, du fikk {score} av {antall} mulig poeng.")

if __name__ == "__main__":
    main()

'''