from groq import generate_response
def run_activity():
    print("Zero-shot,one-shot & few-shot learning activity")

    category=input("Enter a category (e.g:animal,food,city,etc): ").strip()
    item=input(f"Enter a specific {category} to classify:").strip()
    if not category or not item:
        print("Please fill in both the fields to run the activity")
        return
    
    zero_shot=f"is {item} a {category}?Answer yes or no."
    print("\n===ZERO-SHOT LEARNING===")
    print(f"Response:{generate_response(zero_shot,temperature=0.2,max_tokens=1111)}")

    one_shot=f"""Example:
    Category:fruit
    Item:apple
    Answer:Yes,apple is a fruit
    
    Now you try.
    Category:{category}
    Item:{item}
    Answer:"""
    print("\n===ONE-SHOT LEARNING===")
    print(f"Response:{generate_response(one_shot,temperature=0.2,max_tokens=1111)}")

    few_shot=f"""Example 1:
    Category:fruit
    Item:apple
    Answer:Yes,apple is a fruit

    Now you try.
    Category:{category}
    Item:{item}
    Answer:"""
    print("\n===FEW-SHOT LEARNING===")
    print(f"Response:{generate_response(few_shot,temperature=0.2,max_tokens=1111)}")

    creative_prompt=f"""Write an one-sentence story about the given word.

    Example 1:Word:Moon
    Story:The moon followed her home, as if it knew her secret.

    Word:{item}
    Story:"""
    print("\n===CREATIVE FEW-SHOT LEARNING===")
    print(f"Response:{generate_response(creative_prompt,temperature=0.8,max_tokens=1111)}")

if __name__=="__main__":
    run_activity()