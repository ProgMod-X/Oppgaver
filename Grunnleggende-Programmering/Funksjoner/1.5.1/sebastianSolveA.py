'''
Lag en funksjon som krever én parameter, og returnerer verdi etter følgende matematiske funksjon: f(x) = x⋅x + 3 .

Lag et program som skriver ut verdiene av f(x)  for x mellom 1 og 15 . Programmet skal bruke en løkke og funksjonen du laget over.
'''
x = int(input("X = ")) 

def f(x):
     return x*x+3

print(f(x))