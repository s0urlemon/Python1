def factorial(x):
    '''This is a recursive function to find the factorial  of an integer'''

    if x==0 or x==1:
        return 1

    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print("the factorial of 6:",factorial(6))
print("the factorial of 1:",factorial(1))
print("the factorial of 9:",factorial(9))