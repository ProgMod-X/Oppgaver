import random

num = random.randint(1,1000)
guessed = False
tries = 0

while guessed == False:
    guess = int(input("Guess: "))
    tries += 1
    if num < guess:
        print("Lower")
    elif num > guess:
        print("Higher")
    else:
        print("---------------")
        print("YOU WON!!")
        print(f"Total number of guesses: {tries}")
        guessed = True