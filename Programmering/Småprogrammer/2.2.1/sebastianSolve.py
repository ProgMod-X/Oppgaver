
import random 




vinner_tall = random.randint(1,100)
while True:
    try:
        spiller_gjett = int(input("Gjett: "))
        if spiller_gjett == vinner_tall:
            print("Gratulerer! Du gjettet riktig.")
            break
        elif spiller_gjett < vinner_tall:
            print("Tallet er høyere: ")
        else:
            print("Tallet er lavere: ")
    except ValueError:
        print("Ugyldig. Skriv et heltall.")

