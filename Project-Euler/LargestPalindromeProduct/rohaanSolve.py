b = 0
for i in range(1000):
    for j in range(1000):
        a = i * j
        a = str(a)
        if a == a[::-1] and len(str(i)) == 3 and len(str(j)) == 3 and (int(a) > int(b)):
            print(f"{i}\t{j}\t{a}")
            b = a