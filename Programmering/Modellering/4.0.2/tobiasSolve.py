import matplotlib.pyplot as plt
import numpy as np

def l(x):
    return stigningstall*x + (avgy - (avgx * stigningstall))

def S(line, x_values, y_values):
    sum = 0
    for index in range(len(x_values)):
        sum += abs(line(x_values[index]) - y_values[index])**2
    return sum


# DATASET = [(1,1), (13,4), (11, 9), (4, 3), (5, 6), (8, 9)]
x_values = [1,13,11,4,5,8]
y_values = [1,4,9,3,6,9]

# Finn balansepunkt
xsum = 0
for x in x_values:
    xsum += x
avgx = xsum/len(x_values)

ysum = 0
for y in y_values:
    ysum += y
avgy = ysum/len(y_values)

st_start = float(input("Stigningstall start: "))
st_slutt = float(input("Stigningstall slutt: "))

stigningstall = st_start
S_list = []
st_list = []

while stigningstall < st_slutt:
    S_list.append(S(l, x_values, y_values))
    st_list.append(stigningstall)

    stigningstall += 0.001
    
print(f"Sum = {round(min(S_list), 3)}")
print(f"Stigningstall = {round(st_list[S_list.index(min(S_list))], 3)}")

x = np.linspace(min(x_values), max(x_values))

stigningstall = st_list[S_list.index(min(S_list))]

plt.plot(x_values, y_values, "o", color="r")
plt.plot(x, l(x), color="b")

plt.show()