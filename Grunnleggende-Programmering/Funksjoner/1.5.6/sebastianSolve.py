'''
Uten å bruke de innebygde funksjonene min() og max();

Lag en funksjon  minst()  som returnerer det minste av to tall.
Test funksjonen din.
Lag en funksjon  stoerst()  som returnerer det største av to tall
Test funksjonen din.
'''

x,y=int(input("Første tall: ")),int(input("Andre tall: "))

def minst(x,y):
    if x-y<0:
        return x
    else:
        return y
    
def stoerst(x,y):
    if x-y<0:
        return y
    else:
        return x

print(minst(x,y),"er er minst")

print(stoerst(x,y),"er størst")