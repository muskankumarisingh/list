a=[8,3,5,-3,4,-2,9]
i=0
b=[]
while i<len(a):
	if a[i]<0:
		a[i]=0
	i+=1
j=0
while j<len(a):
		z=j
		while z<len(a):
			if a[z]>0:
				if a[j]>a[z]:
					attemp=a[j]
					a[j]=a[z]
					a[z]=attemp
			z+=1
		j=j+1
print(a)

#Logical questions  sorting Karna hai or haha (- )me koi v number h waha 0 aana Chahiye  Baki sb as ascending descending me hoo