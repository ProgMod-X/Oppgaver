import matplotlib.pyplot as plt

def f(x):
    return 30000 * 1.01**x + 500 * x

x = 0
N = 5 * 12

x_list = []
y_list = []

for i in range(N + 1):
    x_list.append(i)
    y_list.append(f(i))

print(f"Anniken hadde {round(f(N))} penger på konto da hun fylte 20 år")

plt.bar(x_list, y_list)
plt.show()