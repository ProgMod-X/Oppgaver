'''
Et tetraeder er en pyramide der alle sidene er likesidede trekanter.

B:
Tetraedertall (~pyramidetall) nummer n er summen av alle trekanttall fra og med nummer 1 til og med nummer n.

Skriv et program som spør brukeren om hvilket tall hen ønsker, og bruker nøstede løkker til å beregne tallet.
Skriv ut tallet.
''' 

#B) 

tall = int(input("Tall: "))
trekanttall = 0
pyramidetall = 0 
for i in range(1,tall+1):
    trekanttall += i
    
    
    pyramidetall += trekanttall

print(pyramidetall)  



