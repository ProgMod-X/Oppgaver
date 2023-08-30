import random

choices = ["stein", "saks", "papir"]

while True:
    bot_choice = random.randint(0,2)
    
    try:
        user_input = input("Stein, saks eller papir: ")
        
        if user_input not in choices:
            raise ValueError
        
        user_choice = choices.index()
        
    except ValueError:
        print("Du må skrive inn gyldig input: stein, saks eller papir! (ingen store bokstaver)")
        print("------------------------------------------------")