list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', ]
list2= []
i=0
while i<len(list1):
    	j=i
    	list3=[]
    	while j<len(list1):
    		list3.append(list1[j])
    		j=j+3
    	list2.append(list3)
    	i+=1
print(list2)
