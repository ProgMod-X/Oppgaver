# A
# Likningen viser at for hver time blir det tilført 5mg virkestoff
# Samtidig bryter kroppen ned andelen k virkestoff per time
  
import matplotlib.pyplot as plt  

def dM(t, k, M, d):
    return -k * M + d
 
x = 0
y = 100
k = 0
d = 5


x_list = []
y_list = []

while y > 80:
    y = 0
    k += 0.001
    x_list = []
    y_list = []
    for x in range(25):
        y += dM(x, k, y, d)
        x_list.append(x)
        y_list.append(y)
        
print(f"k = {k}")

while y < 150:
    y = 80
    d += 0.001
    for x in range(25, 49):
        y += dM(x, k, y, d)

print(f"d = {d}")

y = 80

for x in range(25, 49):
    y += dM(x, k, y, d)
    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.grid()
plt.show()