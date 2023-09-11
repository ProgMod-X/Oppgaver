'''
Lag et “spill” basert på «sten,scissors, paper» (eng.: «Rock-paper-scissors» ) 
der bruker skriver inn sitt valg og datamaskinen trekker tilfeldig. 
Brukeren skal få beskjed om hvem som vant (eventuelt uavgjort) og hvorfor.
'''
import random

spiller = str(input("rock, paper, scissors, lizard, spock?"))
mot = ["rock", "scissors", "paper", "lizard", "spock"]

stander = random.choice(mot)

if spiller == stander:
    print("det ble uavgjort\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "rock" and stander == "scissors":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "scissors" and stander == "paper":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "paper" and stander == "rock":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "rock" and stander == "lizard":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "scissors" and stander == "lizard":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "lizard" and stander == "paper":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "paper" and stander == "spock":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "lizard" and stander == "spock":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "spock" and stander == "rock":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif spiller == "spock" and stander == "scissors":
     print("Du vant!!!\n du valgte", spiller, "systemet valgte", stander)
elif stander == "rock" and spiller == "scissors":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "scissors" and spiller == "paper":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "paper" and spiller == "rock":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "rock" and spiller == "spock":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "scissors" and spiller == "spock":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "paper" and spiller == "lizard":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "spock" and spiller == "lizard":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "spock" and spiller == "paper":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "lizard" and spiller == "rock":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
elif stander == "lizard" and spiller == "scissors":
     print("Du tapte ;-;\n du valgte", spiller, "systemet valgte", stander)
