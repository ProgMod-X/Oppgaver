import random

stack = []

print(stack)
print("Legger til i stacken")
for i in range(5):
    stack.append(random.randint(20,80))
    print(stack)

print("Fjerner bakerste i stack")
for i in stack:
    print(stack)
    stack.pop()
    
print(stack)