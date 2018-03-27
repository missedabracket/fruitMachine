#Console version
#Fruit machine
import random

def checkWin():
    global credit
    if bar1 == "CHERRY":
        if bar1 == bar2 == bar3:
            print("Win: 3 ", bar1)
            credit+=0.5
        elif bar1 ==  bar2:
            print("Win: 2 ", bar1)
            credit+=0.2
    elif bar1 == "BELL":
        if bar1 == bar2 == bar3:
            print("Win: 3 ", bar1)
            credit+=10.0
    elif bar1 == "LEMON":
        if bar1 == bar2 == bar3:
            print("Win: 3 ", bar1)
            credit+=1.0
    elif bar1 == "STAR":
        if bar1 == bar2 == bar3:
            print("Win: 3 ", bar1)
            credit+=5.0
    elif bar1 == "ORANGE":
        if bar1 == bar2 == bar3:
            print("Win: 3 ", bar1)
            credit+=2.0
    elif bar1 == "SKULL":
        if bar1 == bar2 == bar3:
            print("Unlucky! Lose because of 3 ", bar1)
            credit = 0

fruit = ["CHERRY","BELL","CHERRY","LEMON","ORANGE","CHERRY","STAR","CHERRY","SKULL","ORANGE","CHERRY"]
credit = 2.0
play = input("Press Enter to play or Q to quit: ")
while play != "Q" and play != "q":
    credit = credit - 0.1
    bar1 = random.choice(fruit)
    bar2 = random.choice(fruit)
    bar3 = random.choice(fruit)
    print(bar1,bar2,bar3, end="| ")
    checkWin()
    print("Credit: £{0:4.2f}".format(credit))
    if credit < 0.10:
        print("Out of money!")
        play = "Q"
    else:
        play = input("Press Enter to play or Q to quit: ")
