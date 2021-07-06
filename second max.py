number=[50,40,23,70,56,12,5,10,7]
i=0
max=0
sec_max=0
while i<len(number):
	if number[i]>max:
		sec_max=max
		max=number[i]
	if sec_max<number[i] and max>number[i]:
		sec_max=number[i]
	i=i+1
print(sec_max)

