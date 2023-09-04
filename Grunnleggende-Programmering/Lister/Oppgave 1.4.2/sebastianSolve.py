'''
Lag et program som fyller en liste med tilfeldige tall mellom fra og med 1 til og med 100.

Programmet skal deretter

1: Beregne gjennomsnittet
2: Finne største og minste verdi


Eksempel på utskrift:

```bash
Values: 86, 81, 17, 62, 36, 13, 79, 32, 46, 60
Mean:   51.2
Min:    13
Max:    86
```
'''
import random 


x = []

y = 100

for i in range(y):
    x.append(random.randint(1,100))

x.sort()

a = x[0]
b = x[-1]
c = (sum(x)/y)

print("Verider: ",x,"\n Gjennomsnitt: ",c,"\n Min: ",a,"\n Max: ", b ,"\n Gjennomsnitt: ",c)

