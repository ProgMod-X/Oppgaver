tabell = []

for i in range(13):
    a = []
    for j in range(13):
        b = []
        for k in range(13):
            b.append(i * j * k)
        a.append(b)
    tabell.append(a)

print(tabell[3][5][3])