import math
import matplotlib.pyplot as plt

def f(x):
    return 6.594 * math.e**(0.234 * x)

x = 0
dx = 0.0001
N = 25

y_list = []
x_list = []

while x < N:
    y_list.append(f(x))
    x_list.append(x)
    x += dx

    if(len(y_list) < 2):
        print(x)
        continue

    if (y_list[-1] - y_list[-2]) > 160:
        break

print(f"Det første året økningen Netflix får i inntekter er større enn 160 er {2005 + x}")


plt.plot(x_list, y_list)
plt.grid()
plt.show()