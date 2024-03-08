import matplotlib.pyplot as plt

x = [1, 13, 11, 4, 5, 8]
y = [1, 4, 9, 3, 6, 9]

b_x = sum(x) / len(x)
b_y = sum(y) / len(y)

a = [x[0], y[0]]
b = [x[-1], y[-1]]

s = (b[1] - a[1]) / (b[0] - a[0])


x_linje = [min(x), max(x)]
y_linje = [b_y - s*(b_x - min(x)), b_y + s*(max(x) - b_x)]

plt.plot(x_linje, y_linje, color="green")
plt.plot(x, y, 'o', color="blue")
plt.plot(b_x, b_y, 'o', color="red")

plt.show()
