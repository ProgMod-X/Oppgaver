def f(y):
    return y * 0.01 + 500

N = 60

x_list = []
y_list = []
y = 30000

for i in range(N + 1):
    x_list.append(i)
    y_list.append(y)
    y += f(y)
    
print(round(y-f(y)))
    
