import matplotlib.pyplot as plt

x = [1, 13, 11, 4, 5, 8]
y = [1, 4, 9, 3, 6, 9]

a = [x[0], y[0]]
b = [x[1], y[1]]

s = (b[1] - a[1]) / (b[0] - a[0])

print(s)
