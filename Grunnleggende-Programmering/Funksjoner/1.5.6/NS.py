'''
Lag en funksjon  minst()  som returnerer det minste av to tall.
Test funksjonen din.
'''

a = int(input("Skriv inn det ene tallet"))
b = int(input("skriv inn det andre tallet"))

def minst(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    elif a == b:
        return a, b

def storst(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    elif a == b:
        return a, b

print("det minste tallet er", minst(a, b))
print("det største tallet er", storst(a, b))