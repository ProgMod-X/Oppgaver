'''
A:
Trekanttall nummer n er summen av alle positive heltall fra og med 1 til og med n. Vi visualiserer ofte trekanttallene som antall kuler i figurene under (derav navnet).

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/First_six_triangular_numbers.svg/1920px-First_six_triangular_numbers.svg.png)

Skriv et program som spør brukeren om hvilket tall hen ønsker, og bruker én løkke til å beregne tallet. Skriv ut tallet.
'''

tall = int(input("Tall: "))
x = 0
for i in range(1,tall+1):
    x +=i
print(x)