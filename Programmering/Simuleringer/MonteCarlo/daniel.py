from random import randint

N = 10_000_000
size = 1000
sum = 0
n = 0

while n < N:
    ax = randint(0, size)
    ay = randint(0, size)
    bx = randint(0, size)
    by = randint(0, size)
    dist = ((ax - bx)**2 + (ay-by)**2)**0.5
    sum += dist
    # print(dist)
    n += 1

avg_dist = sum/N
print(avg_dist)