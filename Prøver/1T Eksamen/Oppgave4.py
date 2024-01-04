def f(x):
    return 1/9 * (x + 1) * (x - 6) ** 2

x_min = 0
x_maks = 6

sum = 0

n = 6000
bredde = (x_maks - x_min) / n # Liten bredde

for i in range(n):
    x_venstre = x_min + i * bredde
    print(x_venstre)
    x_hoyre = x_min + (i + 1) * bredde
    h = f((x_venstre + x_hoyre) / 2)
    sum += h * bredde

print("Arealet under grafen er:", sum)
