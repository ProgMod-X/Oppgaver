import math
import matplotlib.pyplot as plt

def f(x):
    return 6.594*math.e**(0.234*x)

x = 0
X = 15
dx = 1

x_list = [x+2005]
y_list = [f(x)]
sum = x
flag = False

while x < X:
    x += dx
    x_list.append(x+2005)
    y_list.append(f(x))
    sum += y_list[-1] * dx
    if y_list[-1] - y_list[-2] > 160 and flag == False:
        print(f"Inntektene økte mer enn 160 milliarder for første gang i {2005+x}")
        flag = True
    
for index in range(len(x_list)):
    plt.bar(x_list[index], y_list[index], align="edge", color="red")

print(f"Summen av inntektene til Netflix fra 2005 til 2020 er {sum} milliarder kroner")

plt.grid()
plt.show()