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
La quizet ha tre vanskelighetsgrader:
Enkel – tall mellom 1 og 10
Middels – tall mellom 1 og 25
Vanskelig – tall mellom 1 og 100
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