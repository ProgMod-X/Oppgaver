import matplotlib.pyplot as plt

def l(x):
    return stigningstall*x + (avgy - (avgx * stigningstall))


x_list = [1, 13, 11, 4, 5, 8]
y_list = [1, 4, 9, 3, 6, 9]

# Finn balansepunkt
xsum = 0
for x in x_list:
    xsum += x
avgx = xsum/len(x_list)

ysum = 0
for y in y_list:
    ysum += y
avgy = ysum/len(y_list)

# Idiotisk måte å finne verdiene lengst på hver sin side
sorted_pairs = sorted(zip(x_list, y_list))
sorted_x_list, sorted_y_list = zip(*sorted_pairs)

stigningstall = (sorted_y_list[len(sorted_y_list)-1] - sorted_y_list[0]) / (max(sorted_x_list) - min(sorted_x_list))

# Finn et estimat for beste linje
linelistx = []
linelisty = []
x = 0
while x < 15:
    linelistx.append(x)
    linelisty.append(l(x))
    x += 0.001

plt.plot(avgx, avgy, "o", color="r")
plt.plot(linelistx, linelisty, color="g")
plt.plot(x_list, y_list, "o", color="b")
plt.show()

while True:
    try:
        stigningstall = float(input("Nytt stigningstall: "))
        
        if stigningstall == None:
            break
        
        linelistx = []
        linelisty = []
        x = 0
        while x < 15:
            linelistx.append(x)
            linelisty.append(l(x))
            x += 0.001
        
        
        plt.plot(avgx, avgy, "o", color="r")
        plt.plot(linelistx, linelisty, color="g")
        plt.plot(x_list, y_list, "o", color="b")
        plt.show()
    except ValueError:
        break