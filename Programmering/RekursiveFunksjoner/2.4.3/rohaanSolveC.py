import matplotlib.pyplot as plt

def s(n):
    k = 1/2
    if n == 1:
        return 1/2
    else:
        return 1/2 * ((k**n - 1)/(k - 1))
    
print(s(100))

x, y = [], []

for i in range(20):
    x.append(i)
    y.append(s(i))

plt.plot(x, y)
plt.show()