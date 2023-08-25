n = int(input("Skriv inn en verdi for n: "))

sum = 0

# Utfør løkken for i fra 1 til n
for i in range(1, n + 1):
    term = 2 * i + 1
    sum += term

# Skriv ut resultatet
print(sum)