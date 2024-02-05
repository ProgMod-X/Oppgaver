import matplotlib.pyplot as plt

def f(x):
    return 2 * x - 3 * x**3

def find_intersections(function, start_x, c, n):
    intersections = []
    x = start_x
    y = function(x)
    x_max = 40
    dx = 0.001
    prev_y = function(x - dx)
    while x < x_max and len(intersections) <= n:
        prev_y = y
        y = function(x)
        if (prev_y < c and y > c) or prev_y > c and y < c:
            intersections.append(x)
        x += dx
    return intersections

c = 0
cmaks = 1
dc = 0.001

x = 0
dx = 0.001
xmaks = 1

area = 0

while True:
    x = 0
    area = 0
    intervals = find_intersections(f, x, c, 2)
    
    if len(intervals) < 2:
        c += dc
        continue

    while x < intervals[1]:
        y = f(x)
        if y < c:
            area -= y * dx
        else:
            area += y * dx
        x += dx
    print(area, intervals, c-0.14)

    if round(area, 3) == 0:
        print(c-0.14, round(area, 3), area)
        break 

    c += dc



plt.plot(x_list, y_list)
plt.hlines(c, 0, xmaks, "r")
plt.show()