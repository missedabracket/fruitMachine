#GUI VERSION
from guizero import App, Box, Text, Picture, PushButton
import random

#Actions
def checkWin():
    global credit
    credit = float(creditMoney.value[:4])
    if bar1.value == "cherry.png":
        if bar1.value == bar2.value == bar3.value:
            print("Win: 3 ", bar1.value)
            credit+=0.5
        elif bar1.value == bar2.value:
            print("Win: 2 ", bar1.value)
            credit+=0.2
    elif bar1.value == "bar.png":
        if bar1.value == bar2.value == bar3.value:
            print("Win: 3 ", bar1.value)
            credit+=10.0
    elif bar1.value == "lemon.png":
        if bar1.value == bar2.value == bar3.value:
            print("Win: 3 ", bar1.value)
            credit+=1.0
    elif bar1.value == "orange.png":
        if bar1.value == bar2.value == bar3.value:
            print("Win: 3 ", bar1.value)
            credit+=2.0
    elif bar1.value == "skull.png":
        if bar1.value == bar2.value == bar3.value:
            print("Unlucky! Lose because of 3 ", bar1.value)
            credit = 0
    credit = str(credit)
    credit = credit[:4]
    creditMoney.value = credit

def spinBars():
    global credit
    credit = float(creditMoney.value)
    credit -= 0.20
    credit = str(credit)
    credit = credit[:4]
    creditMoney.value = credit
    bar1.value = random.choice(fruit)
    bar2.value = random.choice(fruit)
    bar3.value = random.choice(fruit)
    checkWin()

def updateBalance():
    global credit
    credit = float(creditMoney.value)
    credit = str(credit)
    credit = credit[:4]

credit = 2.00
fruit = ["cherry.png","bar.png","cherry.png","lemon.png","orange.png","cherry.png","lemon.png","cherry.png","skull.png","orange.png","cherry.png"]
#Windows and Boxes
fruitMachine = App(title="Fruit Machine",width=400,height=600,layout="grid")
myMoney = Box(fruitMachine,layout="grid",grid=[0,0])
myButtons = Box(fruitMachine,layout="grid",grid=[0,1])
extraButtons = Box(fruitMachine,layout="grid",grid=[0,2])

#Text
creditText = Text(myMoney,text="CREDIT: £",size=16,grid=[0,0])
creditMoney = Text(myMoney,text=credit,size=16,grid=[1,0])

#Create and display bars
bar1 = Picture(myButtons,image="cherry.png",grid=[0,0])
bar2 = Picture(myButtons,image="cherry.png",grid=[1,0])
bar3 = Picture(myButtons,image="cherry.png",grid=[2,0])
spin = PushButton(myButtons,command=spinBars,text="SPIN",grid=[3,1])

#Run event loop for program
fruitMachine.display()
