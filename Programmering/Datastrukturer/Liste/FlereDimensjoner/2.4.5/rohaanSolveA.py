tabell = []

for i in range(13):
    a = []
    for j in range(13):
        a.append(i * j)
    tabell.append(a)

print(tabell[3][5])