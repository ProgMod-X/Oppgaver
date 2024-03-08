import matplotlib.pyplot as plt

def deltaY(k, y, w):
    return (k * y) + w

factor = 0.06
change = 6000
balance = 0

x_list = []
y_list = []

for i in range(1, 11):
    balance += deltaY(factor, balance, change)
    x_list.append(i)
    y_list.append(balance)

print(f"Verdien på Camillas andel er {round(balance, 2)} kr dagen før hun fylte 11 år")    

change = 12000

for i in range(11, 21):
    balance += deltaY(factor, balance, change)
    change *= 1.05
    x_list.append(i)
    y_list.append(balance)

print(f"Camillas andel ved det siste inskuddet er verdt {round(balance, 2)} kr")

plt.plot(x_list, y_list)
plt.grid()
plt.show()