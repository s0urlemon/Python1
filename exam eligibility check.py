medical_cause=input("Do you have the medical certificate?Yes or No: ")
atten=int(input("Enter the attendance of the student:"))
if medical_cause=="Yes":
    print("You are allowed.")

else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")