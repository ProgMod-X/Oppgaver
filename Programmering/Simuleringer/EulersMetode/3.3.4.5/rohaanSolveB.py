import matplotlib.pyplot as plt

def f(kropp):
    return kropp * 0.75 + 2.4

kropp = 0

x_list = []
y_list = []

for i in range(100):
    kropp = f(kropp)
    x_list.append(i)
    y_list.append(kropp)

print(kropp)

plt.plot(x_list, y_list)
plt.show()