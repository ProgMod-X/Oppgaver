import random

hovedtall = []
tilleggstall = []

for i in range(7):
    if i >= 5:
        tilleggstall.append(random.randint(1,42))
    else:
        hovedtall.append(random.randint(1,42))

hovedtall.sort()
tilleggstall.sort()

print(hovedtall, tilleggstall)