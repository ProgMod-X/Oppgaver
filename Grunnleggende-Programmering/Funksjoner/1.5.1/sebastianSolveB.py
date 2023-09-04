'''
Lag et program som skriver ut verdiene av f(x)  for x mellom 1 og 15 . Programmet skal bruke en løkke og funksjonen du laget over.

'''



def f(x):
     return x*x+3
i=1
while True:
    print(f(i))
    i+=1
    if i>16:
        break