import random
class FruitQuiz:
    def __init__(self):
        self.fruits={"apple":"red",
                     "orange":"orange",
                     "banana":"yellow"}
        
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))

            print("What is the color of {}".format(fruit))
            user_answer=input()

            if (user_answer.lower()==color):
                print("Correct answer")
            else:
                print("Wrong answer")

            option=int(int(input("Enter 0 if you want to play again,otherwise press 1:")))
            if (option):
                break

print("Welcome to fruit quiz")
fq=FruitQuiz()
fq.quiz()