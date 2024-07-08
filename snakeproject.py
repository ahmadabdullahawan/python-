# 1 for snake -1 for water 0 for gun
import random

Computer = random.choice([-1, 0, 1])
yourstr = input("enter your choice")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1 : "snake", -1 : "water" ,0 :"gun"}
you = youDict[yourstr]
print(f"you chose {reverseDict[you]} and computer chosen{reverseDict[Computer]}")
if (Computer ==you ) :
    print("its a draw")
else:
    if (Computer == -1 and you == 1):
       print("you win")
    elif (Computer==-1 and you==0):
        print("you lose")
    elif (Computer==1 and you==-1):
        print("y lose")
    elif (Computer==1 and you==0):
        print("you win")
    elif(Computer==0 and you==-1):
        print("you win")
    elif(Computer==0 and you==1):
        print("you lose")
    else:
        print("mismatch")

