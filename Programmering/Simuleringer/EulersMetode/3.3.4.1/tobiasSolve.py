def deltaY(k, y, w):
    return (k * y) + w

interest = 0.001
change = 500
balance = 30000

for i in range(1, 61):
    balance += deltaY(interest, balance, change)
    
print(round(balance, 2))