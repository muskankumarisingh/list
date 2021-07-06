list = [
    "How many continents are there?",          
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal ", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list = [3, 4, 1] 
i= 0
while i<len(list):
	print(i+1,list[i])	
	a= 0
	while a<=len(options_list):
		print(a+1,options_list[i][a])
		a= a+1
	j= int(input('enter the solution'))
	if j==solution_list[i]:
			print('congratulation')
	else:
			print("apka jawab galat hai")
			break
	i=i+1

#Saral questions *Koun Banega Codepati(KBC) Without using 5050 lifeline*❤️🥳❣️😊