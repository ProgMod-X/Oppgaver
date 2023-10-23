a = 1001
b = 0
c = 0

for i in range(b, a):
    for j in range(b, a):
        for k in range(b, a):
            if (i + j + k == 1000) and (i < j < k) and (i**2 + j**2 == k**2):
                print(f"\n\n\n\n{i}\t{j}\t{k}\t{i*j*k}")
                c = i*j*k
                break

print(c)