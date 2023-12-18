import random as rnd
counter, width, height = 0, 5, 6
N = 10000000
for i in range(N):
    m1 = (rnd.random() * width, 0)
    m2 = (rnd.random() * width, height)
    p1 = (rnd.random() * width, rnd.random() * height)
    p2 = (rnd.random() * width, rnd.random() * height)

    sm = (m2[1]  - m1[1]) / (m2[0] - m1[0])
    sp = (p2[1]  - p1[1]) / (p2[0] - p1[0])

    if (p1[0] * sp < p1[0] * sm) and (p2[0] * sp > p2[0] * sm):
        counter += 1
    elif (p1[0] * sp > p1[0] * sm) and (p2[0] * sp < p2[0] * sm):
        counter += 1

    # print((p1[0] * sp), ( p1[0] * sm), (p2[0] * sp) , p2[0] * sm)
    print(sm, sp)

print(counter)
print(f"{counter / N * 100}%")
