'''
Lag et program der brukeren skal gjette et heltall. Tallet velger du og skriver i koden.

Tilbakemeldingen til brukeren skal variere etter om;

tallet er riktig
tallet er lavere
tallet er høyre

'''

#import random 
#vinner_tall = random.randint(1,100)

#Du kan legge inn et tilfeldig vinnertall ved å gjøre slik

vinner_tall = 85

#Hvis ikke definerer du vinnertallet

while True:

#"While True" får programmet til å kjøre 
    try:

#"Try får den bare til å kjøre gjennom flere ganger"

        spiller_gjett = int(input("Gjett: "))

#Spør om et gjett
        
        if spiller_gjett == vinner_tall:
            print("Gratulerer! Du gjettet riktig.")
            break

#Hvis spiller gjettet riktig skal programmet printe at de vant og avslutte programmet 

        elif spiller_gjett < vinner_tall:
            print("Prøv høyere: ")

#Hvis gjettet var for lavt sier vi at de skal gjette et høyere tall 

        else:
            print("Prøv lavere: ")
            
#Hvis tallet er høyere sier vi at de skal gjette lavere

    except ValueError:
        print("Ugyldig. Skriv et heltall.")
        
#Hvis spiller skriver inn noe som ikke er gyldig, altså ikke en integer, svarer programmet med å si at det var ugyldig 
