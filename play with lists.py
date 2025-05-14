L=[4,5,8,3,1,2,9,7,10,6]
print("Original list:",L)
count=0
for i in L:
    count+=i
avg=count/len(L)
print("sum=",count)
print("average=",avg)
L.sort()
print("Smallest element in the list:",L[0])
print("Largest element in the list:",L[-1])