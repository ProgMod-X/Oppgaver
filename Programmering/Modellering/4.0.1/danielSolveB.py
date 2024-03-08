import matplotlib.pyplot as plt

x = [1, 13, 11, 4, 5, 8]
y = [1, 4, 9, 3, 6, 9]

b_x = sum(x) / len(x)
b_y = sum(y) / len(y)

print(f"Punktet er i ({b_x}, {round(b_y, 2)})")

plt.plot(x, y, 'o', color="blue")
plt.plot(b_x, b_y, 'o', color="red")
plt.show()