import random

def move(direction):
	if direction=="w":
		if Jim_Hawkins[1]==0:
			print "\n" + "There is the sea there!"
			return True
		else:
			Jim_Hawkins[1]-=1
			return False
	elif direction=="s":
		if Jim_Hawkins[1]==9:
			print "\n" + "There is the sea there!"
			return True
		else:
			Jim_Hawkins[1]+=1
			return False
	elif direction=="d":
		if Jim_Hawkins[0]==9:
			print "\n" + "There is the sea there!"
			return True
		else:	
			Jim_Hawkins[0]+=1
			return False
	elif direction=="a":
		if Jim_Hawkins[0]==0:
			print "\n" + "There is the sea there!"
			return True
		else:	
			Jim_Hawkins[0]-=1
			return False
	else:
		print("\n" + "Use only the W A S D keys!")
		return True
		
def checkForFinding(a,b):
	if a==b:
		print "TREASURE FOUND!!!"
		return True
	else:
		return False

flag="y"
while flag!="n":
        Treasure_Island=[]      #creation of the Treasure_Island
        for x in range(10):
                for y in range(10):
                        Treasure_Island.append([x,y])

        random.shuffle(Treasure_Island)
        treasure=Treasure_Island.pop(0)
        Jim_Hawkins=Treasure_Island.pop(0)

        print "Your coordinates are", Jim_Hawkins
        raw_input("Turn off Caps Lock. (press Enter to continue...)")
        print "\n" + "Using the W(up), S(down), D(right), A(left) keys..."
        while not checkForFinding(Jim_Hawkins,treasure):
                direction = raw_input("Choose direction and press ENTER: ")
                move(direction)
                distance=abs(Jim_Hawkins[0] - treasure[0]) + abs(Jim_Hawkins[1] - treasure[1])
                print "\n" + "You're ", distance, " blocks away from the treasure :("
        flag=raw_input("\n" + "Do you want to restart the game ??? (y/n) ")
