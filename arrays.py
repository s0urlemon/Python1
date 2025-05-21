import array as arr
num=arr.array("i",[1,3,5,7,3,5,7,5,7])
print("Original array:"+str(num))

print("Number of occurrences of the number 3 in the salid array"+str(num.count(3)))

num.reverse()
print("Reverse the order  of the items:")
print(str(num))