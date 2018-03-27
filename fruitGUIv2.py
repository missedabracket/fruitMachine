#GUI VERSION
from guizero import App, Box, Text, Picture, PushButton, info,warn
import random

#Actions
def checkWin():
    global credit
    credit = round(float(creditMoney.value[:4]),2)
    if bar1.value == "cherry.png":
        if bar1.value == bar2.value == bar3.value:
            info("Win: 3 ", "50p")
            credit+=0.5
        elif bar1.value == bar2.value:
            info("Win: 2 ", "20p")
            credit+=0.2
    elif bar1.value == "bar.png":
        if bar1.value == bar2.value == bar3.value:
            info("Win: 3 ", "£10")
            credit+=10.0
    elif bar1.value == "lemon.png":
        if bar1.value == bar2.value == bar3.value:
            info("Win: 3 ", "£1")
            credit+=1.0
    elif bar1.value == "orange.png":
        if bar1.value == bar2.value == bar3.value:
            info("Win: 3 ", "£2")
            credit+=2.0
    elif bar1.value == "skull.png":
        if bar1.value == bar2.value == bar3.value:
            info("Unlucky!", "Lose all your money!")
            credit = 0
    credit = str(credit)
    credit = credit[:4]
    creditMoney.value = credit

    #Carry out a randon spin
def randomSpin():
    bar1.value = random.choice(fruit)
    bar2.value = random.choice(fruit)
    bar3.value = random.choice(fruit)

#Stop spinning bars
def stopSpin():
    fruitMachine.cancel(randomSpin)

#Spin bars, simulate turning.
def spinBars():
    global credit
    if creditMoney.value > "0.1":
        credit = round(float(creditMoney.value),2)
        credit -= 0.20
        credit = str(credit)
        credit = credit[:4]
        creditMoney.value = credit
        fruitMachine.repeat(100,randomSpin) #Spin bars, simulate turning.
        fruitMachine.after(500,stopSpin) #Stop turning.
        bar1.value = random.choice(fruit) #Real spin
        bar2.value = random.choice(fruit) #Real spin
        bar3.value = random.choice(fruit) #Real spin
        fruitMachine.after(510,checkWin) #Call check win once stopped turning
    else:
        warn("Out of money","You have no money left")
        fruitMachine.destroy()

credit = 2.00
fruit = ["cherry.png","bar.png","cherry.png","lemon.png","orange.png","cherry.png","lemon.png","cherry.png","skull.png","orange.png","cherry.png"]
#Windows and Boxes
fruitMachine = App(title="Fruit Machine",width=400,height=600,layout="grid")
myMoney = Box(fruitMachine,layout="grid",grid=[0,0])
myButtons = Box(fruitMachine,layout="grid",grid=[0,1])
extraButtons = Box(fruitMachine,layout="grid",grid=[0,2])

#Text
creditText = Text(myMoney,text="CREDIT: £",size=16,grid=[0,0])
creditMoney = Text(myMoney,text="2.0",size=16,grid=[1,0])

#Create and display bars
bar1 = Picture(myButtons,image="cherry.png",grid=[0,0])
bar2 = Picture(myButtons,image="cherry.png",grid=[1,0])
bar3 = Picture(myButtons,image="cherry.png",grid=[2,0])
spin = PushButton(myButtons,command=spinBars,text="SPIN",grid=[3,1])

fruitMachine.after(10,randomSpin)
#Run event loop for program
fruitMachine.display()
