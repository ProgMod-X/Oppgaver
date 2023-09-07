import random

a = random.randint(1, 10)
b = random.randint(1, 10)


while True:
    c = int(input(f"Hva er produktet av {a} og {b}: "))

    if c == a * b:
        print("Det stemmer")
        break