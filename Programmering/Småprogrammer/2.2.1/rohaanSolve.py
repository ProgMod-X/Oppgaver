import random

tries = 0
system_choice = random.randint(1,100)


while True:
    a = int(input("Gjett: "))

    if a == system_choice:
        break
    elif a > system_choice:
        print("Tallet er lavere")
    else:
        print("Tallet er høyere")

print("Tallet er riktig")