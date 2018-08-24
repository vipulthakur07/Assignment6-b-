#Question-1
a=eval(input('enter the dic :'))
b=int(input("enter the value :"))
flag=False
for i in a.items():
    
    if(b==i[1]):
        
        print(i[0])
#Question-2
a={}
for i in range(2):
    stu=input("enter student name :")
    for b in range(2):
        sub=input("enter subject : ")
        marks=input("enter marks :")
        
        a[stu,sub]=[sub,marks]
name=input("enter name :")
for b in a.items():
    for r in range(2):
        if(b[r][0]==name):
            print(b[1])
