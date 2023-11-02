from math import sqrt
import time

num = 600851475143
primelist = []

for i in range(2, int(sqrt(num))+1):
    prime = True
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            prime = False
            break
    if prime == True:
        primelist.append(i)
        
for i in range(len(primelist)):
    if num % primelist[-i] == 0:
        print(primelist[-i])