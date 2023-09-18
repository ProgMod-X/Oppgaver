import random

choices = ["stein", "saks", "papir"]

while True:
    bot_choice = random.randint(0,2)
    
    try:
        user_input = input("Stein, saks eller papir: ").lower()
        
        if user_input not in choices:
            raise ValueError
        
        user_choice = choices.index(user_input)
        difference = (user_choice - bot_choice) % 3
        
        if difference == 0:
            print(f"Uavgjort! Både du og boten valgte {choices[user_choice]}")
        elif difference == 1:
            print(f"Boten vant! Ditt valg: {choices[user_choice]}, Boten valgte: {choices[bot_choice]}")
        else:
            print(f"Du vant! Ditt valg: {choices[user_choice]}, Boten valgte: {choices[bot_choice]}")
        print("------------------------------------------------")
        break
       
    except ValueError:
        print("Du må skrive inn gyldig input: stein, saks eller papir!")
        print("------------------------------------------------")