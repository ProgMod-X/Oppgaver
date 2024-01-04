import matplotlib.pyplot as plt

def df(x):
    return (9*x**2 - 2*x -2)

dx = 0.5       
x = -1
y = -2
end = 1

x_values = []
Fy_values = []
dfy_values = []

while x < 4:
    Fy_values.append(y)
    dfy_values.append(df(x))
    y += df(x+dx)
    x += dx
    x_values.append(x)

plt.plot(x_values, Fy_values, color="red")
plt.plot(x_values, dfy_values, color="blue")
plt.show()