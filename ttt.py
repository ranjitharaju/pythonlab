a=[1,2,3,4,5,6,7,8,9]
def printboard():	
	print(a[0],'|',a[1],'|',a[2])
	print("---------------")
	print(a[3],'|',a[4],'|',a[5])
	print("---------------")
	print(a[6],'|',a[7],'|',a[8])  
playeroneturn= True

while True:
	printboard()
	p=int(input("enter the postion number"))	
	if(p in a):
		if playeroneturn:
			#p=input("choose your place,player 1>>")
			print("player 1 chose:",p)
			a[int(p)-1]="x"
			playeroneturn= not playeroneturn
		else:
			#p=input("choose your place,player 2>>")
			print("player  chose:",p)
			a[int(p)-1]="o"
			playeroneturn= not playeroneturn

		for i in (0,3,6):
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				if a[i]=='x':
					print("player 1 wins")
					exit()
				else:
					print("player 2 wins!")
					exit()
		for i in range(3):
			if (a[i]==a[i+1] and  a[i]==a[i+2]):
				if a[i]=='x':
					print("player 1 wins")
					exit()
				else:
					print("player 2 wins")
					exit()			

	else:
		continue