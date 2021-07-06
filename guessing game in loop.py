n=3
i=3
while i>=1:
	num=int(input('enter the number'))
	if n==num:
		print('you are right')
		break
	else:
		print('you are wrong you have',i-1,'chance more')
	i-=1