'''
Skriv et program som leser inn temperatur i grader fahrenheit, og skriver ut temperaturen i grader celsius. Rund av utskriften til én desimal.

Bruk formelen c = 5/9(F - 32)
''' 

Temp_F = int(input("Fahrenheit: "))

#Spør om input som integer og definerer den som "Temp_F"

Temp_C = (Temp_F - 32) * 5/9

#Definere "Temp_C" som inputen omregnet til celcius

print(Temp_C)

#Printer inputen i celcius