import random
while True:
    u=input("Enter a choice (rock,paper,scissor):")
    p=["rock","paper","scissor"]
    c=random.choice(p)
    print(f"\nYou chose {u},whereas the computer chose {c}.\n")

    if u==c:
        print(f"Both players chose {u}.Hence,it's a tie")
    
    elif u=="rock":
        if c=="scissor":
            print("Rock beats scissor,you win!!")
        else:
            print("Paper beats rock,you lose..")
    
    elif u=="scissor":
        if c=="rock":
            print("Rock beats scissor,you lose..")
        else:
            print("Scissor beats paper,you win!!")

    elif u=="paper":
        if c=="scissor":
            print("Scissor beats paper,you lose..")
        else:
            print("Paper beats rock,you win!!")

    else:
        print("Wrong input entered,try again..")