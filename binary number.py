b=[1,0,0,1,1,0,1,1]
a=0
i=-1
sum=0
while i>=(-len(b)):
	sum=sum+(b[i]*2**a)
	a=a+1
	i=i-1
print(sum)