import random

a = []
n = 10

for i in range(n):
    a.append(random.randint(1,100))

mean = sum(a)/n
a.sort()

print(f"Values: {a}\nMean: {mean}\nMin: {a[0]}\nMax: {a[n - 1]}")