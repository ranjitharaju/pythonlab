n=0
import random
while (n<100):
    #n=(input("Enter r to roll the dice,or q to quit:"))
    a=input("enter r or q")
    if(a=='r'):
        r=random.randint(1,6)
        n=n+r
        print("dice number and the number you are on is",r,n)
        if (n==8):
        	n=37
        	print("u have got a ladder, clim it up")
        elif(n==13):
        	n=34
        	print("u have got a ladder, clim it up")
        elif(n==40):
        	n=68
        	print("u have got a ladder, clim it up")
        elif(n==52):
        	n=81
        	print("u have got a ladder, clim it up")
        elif(n==76):
        	n=97
        	print("u have got a ladder, clim it up")
        elif(n==11):
        	n=2
        	print("u r caught by a snake, go down")
        elif(n==25):
        	n=4
        	print("u r caught by a snake, go down")
        elif(n==38):
        	n=9
        	print("u r caught by a snake, go down")
        elif(n==65):
        	n=46
        	print("u r caught by a snake, go down")
        elif(n==89):
        	n=70
        	print("u r caught by a snake, go down")
        elif(n==93):
        	n=64									
        	print("u r caught by a snake, go down")
        elif(n==100):
        	print("congrats, u r the winner")
        elif(n>100):
        	n=n-r
        	print("should get valid number to reach 100")		
    else:
         break