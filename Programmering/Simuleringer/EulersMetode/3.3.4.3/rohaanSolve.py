import matplotlib.pyplot as plt

def f(saldo, i):
    if i < 11:
        w = 6000
    else:
        w = 12000 * 1.05**(i - 11)    
    return saldo * 0.06 + w

saldo = 0
x_list = []
y_list = []

for i in range(1, 21):
    saldo += f(saldo, i)
    x_list.append(i)
    y_list.append(saldo)
    if i == 10:
        print(f"Verdien på Camillas aksjefond dør hun fylte 11 år var {saldo}")
    elif i == 20:
        print(f"Verdien på Camillas aksjefond dør hun fylte 20 år var {saldo}")

plt.plot(x_list, y_list)
plt.show()