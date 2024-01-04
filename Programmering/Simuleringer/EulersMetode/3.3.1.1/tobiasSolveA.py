import matplotlib.pyplot as plt

def df(x):
    return (0.5)

dx = 0.001
x = -4
y = 0
end = 4 

x_values = [i for i in range(int((end-x)/dx)+1)]
Fy_values = []
dfy_values = []

while x < 4:
    Fy_values.append(y)
    dfy_values.append(df(x))
    y += df(x+dx)
    x += dx

plt.plot(x_values, Fy_values, color="red")
plt.plot(x_values, dfy_values, color="blue")
plt.show()