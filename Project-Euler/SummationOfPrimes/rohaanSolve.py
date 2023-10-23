from math import sqrt

sum = 0

for i in range(2000000 + 1):
    if i > 1:
        for j in range(2, int(sqrt(i)) + 1):
            if (i % j) == 0:
                break
        else:
            sum += i
            print(i)

print(sum)