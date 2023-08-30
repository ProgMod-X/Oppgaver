import random

while True:
    bot_guess = random.choice(["stein", "saks", "papir"])
    
    try:
        user_guess = input("Stein, saks eller papir: ")
        
    except: