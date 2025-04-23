def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("Please select the operation")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")

choice=input("Please enter yor choise from 'a/b/c/d : ")
num1=int(input("Please enter the first number:"))
num2=int(input("Please enter the second number:"))

if choice=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("This is an invalid input.")