balance = 10000


for i in range(5):
    balance += balance*0.1
    
print(f"Balanse på kontoen etter 5 år er {balance}kr")

balance = 10000
counter = 0
while balance < 20000:
    balance += balance * 0.1
    counter += 1
    
print(f"Det tar {counter} år å nå 20000kr på kontoen, da er balansen på {round(balance, 2)}kr")