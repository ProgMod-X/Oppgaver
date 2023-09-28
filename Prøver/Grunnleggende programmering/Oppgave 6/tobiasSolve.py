import random
sum = 0
counter = 0
while sum <= 2023:
    sum += random.randint(13, 37)
    counter += 1

print(f"Det trengs {counter} tall før summen er større enn 2023")