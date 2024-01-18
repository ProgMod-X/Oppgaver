import math
import matplotlib.pyplot as plt

def f(x):
    return 42*(1-math.e**(-x)) + 1.05*x

x = 0
X = 10
dx = 0.001

x_list = [x]
y_list = [f(x)]
sum = x
flag1 = False
flag2 = False

while x < X:
    x += dx
    x_list.append(x)
    y_list.append(f(x))
    sum += y_list[-1] * dx
    if x >= 3 and flag1 == False:
        print(f"Treningseffekten etter 3 minutter er {round(y_list[-1], 2)} kJ/min")
        flag1 = True
    if y_list[-1] >= 50 and flag2 == False:
        print(f"Treningseffekten er 50 kJ/min etter {round(x, 2)} min")
        flag2 = True

print(f"Det samlede energiforbruket i løpet av de første 10 minuttene er {round(sum, 2)} kJ")


x = 0
x_list = [x]
y_list = [f(x)]
sum = x
while sum <= 1300:
    x += dx
    x_list.append(x)
    y_list.append(f(x))
    sum += y_list[-1] * dx
    
print(f"Hun må trene i {round(x, 2)} minutter for at det samlede energiforbruket skal være 1300 kJ")

plt.plot(x_list, y_list)
plt.grid()
plt.show()