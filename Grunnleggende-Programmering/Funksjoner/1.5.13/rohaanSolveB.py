a = int(input("Hva er a? "))
b = int(input("Hva er b? "))

def congruent(a, b, modulus):
    if a % modulus == b % modulus:
        return True
    else:
        return False
    
if a > b:
    c = b
else:
    c = a

for i in range(1, c + 1):
    if congruent(a, b, i):
        print(i)