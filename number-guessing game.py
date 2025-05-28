import random
import time

nr=random.randint(1,100)

def intro():
    print("May I know your name?")
    global name
    name=input()
    print(name+",we are going to play a game..I will be thinking of a number between 1 and 100")
    if (nr%2==0):
        x="even"
    else:
        x="odd"
    
    print("\nThis is an {} number.".format(x))
    time.sleep(.5)
    print("Go ahead and guess!")
def pick():
    guessestaken=0
    while guessestaken<6:
        time.sleep(.25)
        enter=input("Guess: ")

        try:
            guess =int(enter)
            if guess<=100 and guess>=1:
                guessestaken=guessestaken+1
                if guessestaken<6:
                    if guess<nr:
                        print("The guess of the number you have entered is too low")
                    if guess>nr:
                        print("The guess of the number you have entered is too high")

                    if guess !=nr:
                        time.sleep(.5)
                        print("Try again!")
                    if guess==nr:
                        break

            if guess>100 and guess<1:
                print("Silly goose!That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")

        except:
            print("I dont think"+enter+"is a number..")
    if guess==nr:
        guess=str(guessestaken)
        print("Good job,{}! You guessed my number in {} guesses.".format(name,guessestaken))
    if guess!=nr:
        print("Nope.The number I was thinking about was "+str(nr))

playagain="yes"
while playagain=="yes" or playagain=="YES":
    intro()
    pick()
    print("Do you want to play again?")
    playagain=input()