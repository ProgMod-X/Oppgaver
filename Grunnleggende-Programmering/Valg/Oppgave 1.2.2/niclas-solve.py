# Velg et tilfeldig heltall som brukeren skal gjette
import random
hidden_number = int(random.randint(1, 100))

while True:
    try:
        guess = int(input("Gjett et heltall: "))
        
        if guess == hidden_number:
            print("Gratulerer! Du gjettet riktig.")
            break
        elif guess < hidden_number:
            print("Tallet er lavere enn det skjulte tallet. Prøv igjen.")
        else:
            print("Tallet er høyere enn det skjulte tallet. Prøv igjen.")
    except ValueError:
        print("Ugyldig inntasting. Skriv inn et heltall.")