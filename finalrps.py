p=0
q=0
while (q<10) and (p<10):
	take=int(input("enter the option 1 for rock, 2 for paper, 3 for scissor"))
	t={1:'rock',2:'paper',3:'scissor'}
	if(take==1):
   		a=(t[1])
	elif(take==2):
   		a=(t[2])
	elif(take==3):
   		a=(t[3])
	else:
		print("inavlid entry")
		exit()
	print("user:",a)	
  
	import random
	r=random.randint(1,3)
	if(r==1):
   		b=(t[1])
	elif(r==2):
   		b=(t[2])
	elif(r==3):
   		b=(t[3])
		print("computer:",b)

	score=0
	if(a==b):
 		print("its a TIE match")
	elif(a=='rock') and (b=='paper'):
  		print("computer is the winner")
  		score=q+1
	elif(a=='rock') and (b=='scissor'):
  		print("user is the winner")
  		score=p+1
	elif(a=='paper') and (b=='rock'):
  		print("user is the winner")
  		score=p+1
	elif(a=='paper') and (b=='scissor'):
  		print("user is the winner")
  		score=p+1
	elif(a=='scissor') and (b=='rock'):
  		print("computer is the winner")
  		score=q+1
	elif(a=='scissor') and (b=='paper'):
  		print("user is the winner")	
  		score=p+1	
	print(score)
	while(q==10):
		print("computer is the winner")
		exit()
	while(p==10):
		print("user is the winner")
		exit()