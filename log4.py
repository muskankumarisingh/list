a=["A","B"]
b=[]
i=1
n=int(input("enter the number"))
while i<=n:
	j=0
	while j<len(a):
		b=b+[a[j]+str(i)]
		j=j+1
	i=i+1
print(b)

#Logical questions  output: user 2 de to ["A1","B1","A2","B2"]