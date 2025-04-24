def cube(number):
    return number*number*number

def by_seven(number):
    if number%7==0:
        return cube(number)
    else:
        return False
    
print(by_seven(28))
print(by_seven(27))