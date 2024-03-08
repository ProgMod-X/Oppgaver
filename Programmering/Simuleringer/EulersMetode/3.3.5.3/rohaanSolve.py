import matplotlib.pyplot as plt

ansatte = 158
år = 0

x_list = []
y_list = []

while år <= 10:
    x_list.append(år)
    y_list.append(ansatte)

    ansatte += 0.1 * ansatte - 1
    år += 1

print(x_list[-1], y_list[-1])

plt.plot(x_list, y_list)
plt.show()