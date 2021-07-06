a=[1,[5],4,[4],3,[3],2,[3],1,[1]]
a1=[]
a2=[]
sum=0
i=0
while i<len(a):
	if type(a[i])==list:
		a1.append(a[i])
	else:
		a2.append(a[i])
	i+=1
j=0
a3=[]
while j<len(a1):
		e=0
		while e<len(a1[e]):
			if a1[j][e] not in a3:
				a3.append(a1[j][e])
			e+=1
		j+=1
list=a2+a3
print(list)
sum=0
h=0
while h<len(list):
		sum+=list[h]
		h+=1
print(sum)