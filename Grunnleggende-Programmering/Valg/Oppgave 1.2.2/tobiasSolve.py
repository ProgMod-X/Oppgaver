import random

num = random.randint(1,1000)
guessed = False
while guessed == False:
    guess = int(input("Guess: "))
    if num < guess:
        print("lower")
    elif num > guess:
        print("higher")
    else:
        print("Correct")
        guessed = True