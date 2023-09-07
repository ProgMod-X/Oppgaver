max = int(input("Tall opp til: "))
sum = 0

for i in range(0, max+1):
    sum += i
    
print(f"Summen av tallene opp til {max} er {sum}")