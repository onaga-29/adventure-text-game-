name=input("Enter your name:")
print("Hi,welcome "+ name)
print("Let's start the game")
currentRoom='room-29'
stuff=[]
def printCurrentSitution():
	print("---------------------------------")
	print("You are in the "+"((" + currentRoom +"))")
	print("And you have these items(at first you have nothing): ","((",stuff,"))")
	print("---------------------------------")

rooms={
'room-29':{'up':'room-101'},
'room-101':{'down':'room-29','right':'dark-room','left':'e-room'},
'e-room':{'right':'room-101','item':'sword'},
'dark-room':{'left':'room-101','down':'kitchen','right':'room-000','up':'room-2029'},
'room-000':{'left':'dark-room','thing':'monster'},
'kitchen':{'right':'exit','up':'dark-room'},
'room-2029':{'down':'dark-room','item':'key'}
}


while True:
	printCurrentSitution()
	try:
		direction=str(input("Type the direction that you wanna go(up--down--right--left): "))
		currentRoom=rooms[currentRoom][direction]
		if(currentRoom =='exit' and 'key' in stuff):
			print("Welldone,You escaped!")
			break
		elif(currentRoom =='exit' and 'key' not in stuff):
			print("Oops! the door is locked, I think you need a key to escape!")
			currentRoom="kitchen"
		elif('thing' in rooms[currentRoom]):
			print("Looks like something is here...")	
			if(rooms[currentRoom]['thing']=='monster' and 'sword' not in stuff):
				print("Oh,what is this?ohhh my goddd it's a ..........")
				print("Oops,sorry the monster has got you!!! Game Over!")
				break
			elif(rooms[currentRoom]['thing']=='monster' and 'sword' in stuff):
				print("Oh, A Beast!!...I have to fight him with this sword...")
				print("Come on, You dickhead ,come on you idiot f*** ......ahhhhhhhhaaooahhahhh........")
				print("Told you motherf*****,told you that I kill you!!!")
				print("Ok,finally you kill the monster now you can go on")


		elif('item' in rooms[currentRoom]):
			print("Oh, there is item  in this room and the item is: ", rooms[currentRoom]['item'])
			ask_1=input("Wanna get it?(y/n): ")
			if(ask_1=='y'):
				stuff.append(rooms[currentRoom]['item'])
				print("You got the",rooms[currentRoom]['item'])
			elif(ask_1=='n'):
				print("It's ok but maybe you need it later!")
	except:
		print("There is no room in that way, try again")
		
