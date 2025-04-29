import random 
playing =True
number=str(random.randint(0,5))

print("I will generate a number from 0 to 5,and u will have to guess the number one digit at a time")
print("The game ends when you get the number correct")
while playing:
    guess=input("Give me your best guess!\n")
    if number==guess:
        print("You win the game!")
        print("The number was",number)
        break
    else:
        print("Oh no..an incorrect guess,better luck next time")