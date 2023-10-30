from math import sqrt

num = 600851475143
primelist = []
prime = True

for i in range(1, int(1000/2)+1):
    prime = False
    for j in range(1, int(sqrt(i))+1):
        if i % j != 0:
            prime = True
            break
    if prime:
        primelist.append(i)
        
print(primelist)