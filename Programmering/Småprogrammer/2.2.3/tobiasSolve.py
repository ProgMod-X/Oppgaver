import random

def gen_question(diff):
    if diff == "l":
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
    elif diff == "m":
        n1 = random.randint(1, 25)
        n2 = random.randint(1, 25)
    elif diff == "v":
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
    
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        ans = n1 + n2
    elif op == "-":
        ans = n1 - n2
    elif op == "*":
        ans = n1 * n2
    else:
        ans = n1 / n2
    
    return f"{n1} {op} {n2}\n", round(ans, 2)

diff = input("Vanskelighetsgrad (l/m/v): ").lower()

answered = 0
correct = 0
total = int(input("Antall spørsmål: "))

while answered < total:
    q, answer = gen_question(diff)
    
    try:
        useranswer = round(float(input(f"{q} = ")), 2)
    except ValueError:
        print("Svaret må være et tall")
    
    if useranswer == answer:
        print("\nRiktig!\n")
        correct += 1
        answered += 1
    else:
        print("\nFeil\n")
        answered += 1

perc = (correct / total) * 100

print("Resultat:")
print("-----------------------")

if perc == 100:
    print("Perfekt!")
elif perc > 66.6:
    print("Bra!")
elif perc > 33.3:
    print("Du trenger mer trening...")
else:
    print("Spør mattelæreren din om hjelp!")
    
print(f"{perc}% correct")
