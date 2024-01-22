import matplotlib.pyplot as plt

# def f(x):
#     return 30000 * 1.01**x + 500 * x

def f(saldo):
    return saldo * 0.001 + 500

N = 5 * 12

x_list = []
y_list = []
saldo = 30000

for i in range(N + 1):
    x_list.append(i)
    y_list.append(saldo)
    saldo += f(saldo)

print(f"Anniken hadde {round(saldo - f(saldo))} penger på konto da hun fylte 20 år")

plt.bar(x_list, y_list)
plt.show()