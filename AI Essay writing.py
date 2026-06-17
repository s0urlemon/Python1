from hf import generate_response

def get_essay_details():
    print("\n===AI Writing Assistant===\n")
    topic=input("What is the topic of your essay?").strip()
    essay_type=input("What type of essay are you typing?").strip()
    lengths=["250 words",'450 words','700 words','1000 words','2500 words']
    print("Select word limit for the essay:")
    for i,l in enumerate(lengths,1):print(f"{1}){l}")
    try:
        idx=int(input("> ").strip())
        length=lengths[idx-1] if 1 <= idx <=len(lengths) else '450 words'
    except ValueError:
        length='450 words'
    target_audience=input("Target audience(ex:Professors):").strip()
    return{'topic':topic,'essay_type':essay_type,'length':length,'target_audience':target_audience}

def generate_essay_content(details):
    try:
        temp=float(input("Enter temperature(0.1=formal,0.7=creative):").strip())
        if not(0.0<=temp<=1.0): raise ValueError
    except ValueError:
        print("Invalid temperature.Using 0.3")
        temp=0.3

    intro_p=f"Write an introduction for {details['essay_type']} essay about {details['topic']} on the topic of {details['length']}"
    intro=generate_response(intro_p,temperature=temp,max_tokens=1111)
    print("\n===Generated Introduction===\n")
    print(intro)
    print("\nWould you like the body written as a full draft or step-by-step?")
    print("\n1)Full draft\n2)Step-by-step")
    choice=input("> ").strip()

    if choice=="1":
        body_p=f"Write a full body for an essay on {details['topic']} with the stance of {details['target_audience']}"
        body=generate_response(body_p,temperature=temp,max_tokens=1111)
        print(body)