
from random import randrange as rand
from time import sleep as wait

likeliness = str(rand(1,4))
funny = str(rand(1,3))
friends = str(rand(0,1))
hated = str(rand(40,100))

def colourprint(text):
    print("\033[91m{}\033[0m".format(text))

def greenprint(text):
    print("\033[92m{}\033[0m".format(text))


def points():
    colourprint("=-=- Attribute -=-=\nLikeliness:"+likeliness+"/10\nFunniness:"+funny+"/10\nFriends:"+friends+"/NA\nHated:"+hated+"%\n")
    game()


def checkattribute(x):
    if x > 10:
        colourprint("You gained too much of the attribute and now you've lost the game :<")
        exit

def checkhate(x):
    if x >= 100:
        colourprint("You gained too much hate and now you lost the game :<")
        exit


def credits():
    colourprint("\nI'd like to personally thank you for playing my game, I hope you enjoyed!")
    exit

def immigration():
    caught = str(rand(0,40))
    colourprint("It's the day, the day Core tries to immigrate with all his cousins")
    wait(1)
    greenprint("Everyone, today we'll be able to get into the UK!\nI'm sick of Sweden's bad economy!")
    wait(1)
    colourprint("Core gets in the boat and paddles away with all his cousins.")
    wait(4)
    colourprint("Core arrives in the east of the UK and spots some guards doing their nightly shifts, they're armed...")

    if(int(caught) >= 21):
        colourprint("Uh oh, the guards have caught Core trying to immigrate!")
        wait(.5)
        greenprint("WHAT DO I DO, SHALL I RUN??")
        choice2 = input(">")
        if "y" in choice2.lower() and "e" in choice2.lower():
            colourprint("Adam/Core tries to run but he fails because he's 5'6 and fat :<")
            greenprint("This, this is the end. They've caught me.\nI cannot go on longer.\nI cannot skid any longer...\nI will never learn how to type cast...")
            credits()
    else:
        colourprint("Core successfully snuck past them and managed to make it into the UK unoticed")
        wait(4)
        greenprint("FINALLY I'VE MADE IT!")
        wait(3)
        colourprint("5 Years have past since then, Core now works as a janitor with minimum wage.")
        wait(1)
        credits()

def popular():
    global hated
    print("\n")
    greenprint("Who shall I write a thread about?")
    choice = str(input(">"))
    greenprint("That's smart, time to write a thread about " + choice + "!")
    wait(2)
    colourprint("Time passes as core starts stealing your memes that you post to try and act popular")
    wait(2)
    megalul = rand(1,2)
    if(megalul == 1):
        colourprint("What's this? People hated your thread!")
        wait(1)
        greenprint("OMG, WHY ARE PEOPLE DISLIKING MY THREAD?!??!?!")
        wait(1)
        hateincrease = str(rand(1,30))
        colourprint("Hated rises by " + hateincrease + "%!")
        hated = int(hated) + int(hateincrease)
        checkhate(hated)
        game()
    else:
        colourprint("Oh, people enjoyed your thread!")
        wait(1)
        greenprint("haha people are liking me!")
        wait(1)
        hatedecrease = str(rand(1,30))
        colourprint("Hated decreases by " + hatedecrease + "%!")
        hated = int(hated) - int(hatedecrease)
        checkhate(hated)
        game()

def fakemoney():
    print('\n')
    colourprint("Core is on discord saying he has a lot of money and fancy cars when in reality he doesn't..")
    wait(1)
    greenprint("Haha yeah man I'm so rich in real life and I'm not no immgrant!")
    wait(1)
    colourprint("The other lads ask him to show proof...")
    wait(1)
    greenprint("Proof? Easy. Uhh but I really have to go now...")
    wait(1)
    colourprint("Core never replied to them with proof...")
    wait(1)
    greenprint("Phew, that was close they almost found out I was actually broke and unloved XD")
    game()

def game():
    print('\n')
    print("\033[92mHi, my names Adam Bilski but you may know me as ps2boy!\nThis Simulator was written by the lord Pudding Mug\n=-+=-+ Options +-=+-=\nA) Make a thread about people because I want to be popular\nB) Try to immigrate to another country\nC) Check Points\nD) Flex fake money\033[0m")
    choice = str(input(">"))
    if(choice.lower() == "a"):
        popular()
    elif(choice.lower() == "b"):
        immigration()
    elif(choice.lower() == "c"):
        points()
    elif(choice.lower() == "d"):
        fakemoney()

if(__name__ == "__main__"):
    game()
