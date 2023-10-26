gangetabell = []

for i in range(13):
    gangetabell.append([])

for i in range(13):
    for j in range(13):
        gangetabell[i].append(i * j)

print(gangetabell[3][5])

'''
Med while løkke

gangetabell = []

i = 0
while i < 13:
    gangetabell.append([])
    i += 1

i = 0
while i < 13:
    j = 0
    while j < 13:
        gangetabell[i].append(i*j)

print(gangetabell)
'''