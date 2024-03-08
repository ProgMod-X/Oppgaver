import matplotlib.pyplot as plt


def f(y):
    return y * -0.20 + 125

N = 100

x_list = []
y_list = []
y = 125

for i in range(1, N):
    x_list.append(i)
    y_list.append(y)
    y += f(y)
    
plt.plot(x_list, y_list, ".")
plt.hlines(y, 1, 100, "r")
plt.show()    
