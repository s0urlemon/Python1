try:
    num1,num2=eval(input("Enter 2 numbers separated by a comma to divide: "))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("Division by zero is considered as undefined!!")
except SyntaxError:
    print("Comma is missing,kindly separate the numbers by a comma")
except:
    print("Invalid input")
else:
    print("No exceptions")
finally:
    print("This will be printed no matter the output.")