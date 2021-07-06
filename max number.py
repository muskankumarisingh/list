number=[50,40,23,70,56,12,5,10,7]
i=0
c=0
while i<len(number):
	if number[i]>c:
		c=number[i]
	i+=1
print("max number is",c)
