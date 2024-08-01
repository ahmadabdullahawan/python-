#if statement
a=float(input("enter a number"))
if(a % 2 == 0):
    print("its an even number")



#if else
#if statement
a1=float(input("enter a number"))
if(a1 % 2 == 0):
    print("its an even number")
else:
    print("its an odd nmber")

#nested if else
marks=float(input("enter yr marks"))
if (marks>90):
    print("grade A1")
elif (marks>80 and marks<90):
    print('grade b')
elif (marks>70 and marks<80):
    print("grade c")
elif (marks>60 and marks<70):
    print("grade d")
elif (marks>50 and marks<60):
    print("staifactory")
else:
    print('you are failed ')



# nested iflese


age=float(input("Enter the age"))

if(age<18):
    print("Minor Age")
    if(age<15):
        print("You are in School")
    else:
        print("You are in College")
elif(age>=18 and age<=45):
    print("Mid Age")
elif(age>45 and age<=50):
    print("Senior Mid Age")
else:
    print("Senior Citizen")

