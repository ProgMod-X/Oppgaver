import random

stack = []

print("Legger til i stacken")
for i in range(5):
    stack.append(random.randint(20,80))
    print(stack[i])

print("Fjerner bakerste i stack")
for i in stack:
    stack.pop()
    print(stack)