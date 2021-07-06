user =input("enter sentence ")
list=[]
i=0
b=""
while i<len(user):
	if user[i]==" ":
		list.append(b)
		b=""
	else:
		b=b+user[i]
	i=i+1
if b:
    list.append(b)
print(list)
