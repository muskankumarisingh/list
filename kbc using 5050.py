list = ["How many continents are there?","What is the capital of India?",  "Ng mei koun sa course padhaya jata hai"]
opt= [["Four", "Nine", "Seven", " Eight"],[" Chandigarh", "Bhopal", " Chennai", "Delhi"],["Software Engineering", " Counseling", "Tourism", "Agriculture"]]
fiftyfifty=[['four','seven'],['Delhi','Bhopal'],['Tourism','software engineering']]
solution1=[2,1,2]
solution=[3,4,1]
i=0
c=0
while i<len(list):
        print('your question is')
        print(i+1,list[i])
        j=0
        print('your options are')
        while j<=len(opt):
            print(j+1,opt[i][j])
            j +=1
        n=int(input("enter the solution"))
        if n==solution[i]:
            print("congratulation")
        elif n==5050:
            if c==0:
                m=0
                while m<len(fiftyfifty[i]):
                    print(m+1,fiftyfifty[i][m])
                    m=m+1
                c=c+1
                num=int(input("enter the solution"))
                if num==solution1[i]:
                    print('correct')
                else:
                    print("apka jawab galat  hai")
                    break
            else:
                print('you already used 5050 lifeline')
                num1=int(input("enter your option"))
                if num1==solution[i]:
                    print("congratulation")
                else:
                    print("apka jawab galat hai")
                    break
        else:
            print("apka jawab galat hai")
            break    
        i +=1

#Saral questions *Koun Banega Codepati(KBC) Using 5050 lifeline*❤️😊😘🥰