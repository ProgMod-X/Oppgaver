import random

operators = ["+", "-", "*", "/"]
operator = int(input("Hvilken vil du ha?\n +(0), -(1), *(2), /(3), blanding(4): "))
difficulty = int(input("Hvilken vanskelighets grad?\nEnkel(0), Middels(1), Vanskelig(2): "))
n = int(input("Hvor mange spørsmål? "))

if difficulty == 0:
    difficulty = 10
elif difficulty == 1:
    difficulty = 25
elif difficulty == 2:
    difficulty = 100


def game(operator, numbers):

    correct = 0
    for i in range(numbers):
        if operator == 4:
            opr = random.choice(operators)
        else:
            opr = operators[operator]

        a = random.randint(1, difficulty)
        b = random.randint(1, difficulty)
        c = float(input(f"Hva er {a} {opr} {b}: "))

        if (c == a + b and operator == 0) or (c == a + b and operator == 4):
            correct += 1
        elif (c == a - b and operator == 1) or (c == a + b and operator == 4):
            correct += 1
        elif (c == a * b and operator == 2) or (c == a + b and operator == 4):
            correct += 1
        elif (c == round(a / b, 2) and operator == 3) or (c == a + b and operator == 4):
            correct += 1

    return correct

correct = game(operator, n)

if correct == n:
    print("Perfekt", end=" ")
elif correct > n / 3 * 2:
    print("Bra!", end=" ")
elif correct <= n / 3 * 2 and correct >= n / 3:
    print("Du trenger mer trening...", end=" ")
else:
    print("Spør mattelæreren din om hjelp!", end=" ")

print(f"{correct/n*100}% correct")