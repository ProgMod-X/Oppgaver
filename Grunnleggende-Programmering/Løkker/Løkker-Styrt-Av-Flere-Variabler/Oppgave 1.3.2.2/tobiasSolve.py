max = int(input("Tall opp til: "))
sum = 1

for i in range(1, max + 1):
    sum *= i
    
print(f"Summen av tallene opp til {max} multiplisert sammen er {sum}")