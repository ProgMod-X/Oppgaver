n = int(input("Skriv inn en verdi for n: "))
sum = 1

for i in range(1, n + 1):
    term = 2 * i + 1
    print(term)
    sum *= term

print(sum)
