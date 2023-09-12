import random

correct = 0

while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = int(input(f"Hva er produktet av {a} og {b}: "))

    if c == a * b:
        print("Det stemmer")
        correct += 1
    else:
        break

print(f"Du fikk {correct}/{correct + 1} riktige")