'''
A) Skriv et program som skriver ut tall i intervallet [0, 5] med en avstand på 0.5.

B) Legg til en ekstra kolonne i utskriften, bruk \t (tabulator) til å skille kolonnene. I den nye kolonnen skal du bruke funksjonen round() til å runde av tallet til ingen desimaler. 
Hva observerer du?
'''
import numpy as np  

#A)

for x in np.arange(0,5.5, 0.5):
    print(x)
    x += 0.5
    
#B)

for x in np.arange(0,5.5, 0.5):
    print(x, "\t", round(x))
    x += 0.5

