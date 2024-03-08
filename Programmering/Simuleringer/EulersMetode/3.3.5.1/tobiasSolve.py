# A
# Differentiallikningen viser oss hvor mye normal diesel som blir byttet ut med biodiesel
# Vi kan integrere denne likningen for å finne ut hvor mye biodiesel og diesel det er i tanken til en hver tid
  
import matplotlib.pyplot as plt  

def df(x, y):
    return 1 - 0.0025 * y
 
dx = 1
x = 0
y = 0

x_list = []
y_list = []
flag = False

while y < 399:
    y += df(x, y)
    if y >= 200 and flag == False:
        print(f"Han må tappe ut {x} liter for at halvparten av dieselen skal være byttet ut med biodiesel")
        flag = True
    x_list.append(x)
    y_list.append(y)
    x += dx

plt.plot(x_list, y_list)
plt.grid()
plt.show()