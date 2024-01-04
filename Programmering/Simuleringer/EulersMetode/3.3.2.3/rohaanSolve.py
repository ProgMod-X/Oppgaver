import matplotlib.pyplot as plt
import math

# Bruker trapes metoden


def f(x):
    return 1 / x


a = 1
k = 1.01
areal = 0

while round(areal, 6) < 2:
    n = 100
    dx = (k - a) / n
    z = 1

    x = a + (z - 1) * dx
    x_list = []
    y_list = []
    areal = 0


    while x < k:
        areal += abs((f(a + (z - 1) * dx) + f(a + (z) * dx)) / 2 * dx)

        x_list.append(x)
        y_list.append(f(x))

        x += dx
        z += 1

    print(f"Arealet under grafen er {areal}")

    k += 0.0001

print(f"For at flatestykket F skal ha et areal på 2 må k være {round(k, 5)}")

plt.plot(x_list, y_list)
plt.show()
