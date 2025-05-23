num1=[1,2,3,4]
num2=[5,6,7,8]
result=map(lambda x,y:x+y,num1,num2)
print("Addition of two lists")
print(list(result))

nums=[1,2,3,4,5,6]
def sq(n):
    return n*n
square=list(map(sq,nums))
print("original list:")
print(nums)
print("Square of numbers on list")
print(square)