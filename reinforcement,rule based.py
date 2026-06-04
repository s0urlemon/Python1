from groq import generate_response

def reinforcement_learning_activity():
    print("\n===REINFORCEMENT LEARNING ACITIVTY===\n")
    prompt=input("Enter a prompt for the AI model(eg:describe a lion):").strip()
    if not prompt:
        print("Please enter a prompt to run the activity")
        return
    
    initial_response=generate_response(prompt,temperature=0.3,max_tokens=1111)
    print(f"\nInitial AI response:{initial_response}")

    try:
        rating=int(input("Rate the response from 1(bad) to 5(good):").strip())
        if rating<1 or rating>5:
            print("Invalid rating.Use whole numbers.Taking 3")
            rating=3
    except ValueError:
        print("Invalid rating.Use whole numbers.Taking 3")
        rating=3 

    feedback=input("Provide feedback for improvement:").strip()
    improved_response=f"{initial_response}(Improved with your feedback:{feedback})"
    print(f"\nImproved AI response:{improved_response}")

def role_based_prompt_activity():
    print("\n===ROLE-BASED LEARNING ACITIVTY===\n")
    category=input("Enter a category(eg:history,astronomy,etc):").strip()
    item=input(f"Enter a specific topic in {category}(eg:'acrylic painting' in art):").strip()

    if not category or not item:
        print("Please fill in both the fields to run the activity")
        return
    
    student_prompt=f"You are a student.Explain {item} in simple terms."
    expert_prompt=f"You are an expert.Explain {item} in factual terms."

    student_response=generate_response(student_prompt,temperature=0.5,max_tokens=1111)
    expert_response=generate_response(expert_prompt,temperature=0.1,max_tokens=1111)

    print(f"\n===Student's Perspective===\n{student_response}")
    print(f"\n===Expert's Perspective===\n{expert_response}")

def run_activity():
    print("\n===AI Learning Activity===")
    print("Choose an activity")
    print("1. Reinforcement Learning")
    print("2. Role-based Prompts")
    choice=input("> ").strip()

    if choice=="1":
        reinforcement_learning_activity()
    if choice=="2":
        role_based_prompt_activity()
    else:
        print("Invalid choice.Please choose 1 or 2")

if __name__=="__main__":
    run_activity()