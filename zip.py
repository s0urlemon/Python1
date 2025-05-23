s1={4,2,3,1}
s2={"b","a","c"}
s3=list(zip(s1,s2))
print(s3,"\n")

l1=[10,20,30,40]
l2=[400,300,200,100]
for x,y in zip(l1,l2[::-1]):
    print(x,y)

stocks=["reliance","infosys","tcs"]
prices=[2397,1408,4962]
dict={stocks:prices for stocks,
      prices in zip(stocks,prices)}
print("\n{}".format(dict))