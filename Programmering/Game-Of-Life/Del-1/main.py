import random

def populate(width, height):
    tabell = []
    for i in range(width):
        col = [random.randint(0, 1) for j in range(height)]
        tabell.append(col)

    return tabell

print(populate(3, 3))
