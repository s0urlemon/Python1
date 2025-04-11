string=input("Please enter your own string:")

string2=("")
for i in string:
    string2=i+string2

print("\nThe original string:",string)
print("\nThe reversed string:",string2)