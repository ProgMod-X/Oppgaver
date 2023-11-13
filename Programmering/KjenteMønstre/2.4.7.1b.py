import random

queue = []

print(queue)
print("Legger til i queue")
for i in range(5):
    queue.append(random.randint(20,80))
    print(queue)
    
print("Fjerner første i queue")
for i in range(5):
    print(queue)
    queue.pop(0)
    
print(queue)