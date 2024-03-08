import matplotlib.pyplot as plt

medicine_in_body = 0
k = 0.037569

x_list = []
y_list = []

for i in range(49):
    x_list.append(i)
    y_list.append(medicine_in_body)
    medicine_in_body += -k * medicine_in_body + 5

plt.plot(x_list, y_list)
plt.show()