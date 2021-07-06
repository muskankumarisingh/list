number=30
num=[10,11,12,13,14,17,18,19]
a=[]
i=0
while i<len(num):
	j=i
	while j<len(num):
		if num[i]+num[j]==number:
			a.append([num[i],num[j]])
		j=j+1
	i=i+1
print(a)