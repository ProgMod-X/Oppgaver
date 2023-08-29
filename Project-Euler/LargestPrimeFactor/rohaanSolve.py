from math import sqrt

num = 600851475143

for i in range(1, 100000):
    for j in range(2, int(sqrt(i))):
        if (i % j) == 0:
            break
    else:
        if num/i == int(num/i):
            print(f"{num}\t{i}\t{num/i}")