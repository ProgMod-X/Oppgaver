# A
# Ledelsen har antatt at antall ansatte øker med 10% av nåværende ansatte hvert år, samtidig som 1 ansatt forsvinner

def dA(A):
    return 0.1 * A - 1

A = 158

for i in range(10):
    A += dA(A)

print(f"Antall ansatte etter 10 år: {round(A)}")

# De vil være rett under 400 ansatte etter 10 år